#Imports de DJANGO
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO

#Imports de DJANGO-REST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



#Imports del proyecto
from .forms import CreateUserForm, AsignarEmpresaForm
from .decorators import unauthenticated_user, allowed_users, admin_only, client_only, gestion_usuarios
from .models import Alerta, Perfil

#Imports de Python
import csv, io

#Pagina del dashboard
@login_required(login_url='login')
@allowed_users(allowed_roles=['cliente', 'user'])
def Dashboard(request):
	req_user = request.user.id
	empresa = Perfil.objects.get(user__id=req_user)
	empresa = empresa.empresa

	lista_alertas = Alerta.objects.filter(usuario__empresa = empresa)
	lista_alertas = lista_alertas.filter(riesgo = 3)
	lista_alertas = lista_alertas.filter(correo_enviado='f')
	ataques_criticos = lista_alertas.count()

	if lista_alertas:
		lista_emails = Perfil.objects.filter(empresa = empresa)
		lista_emails = lista_emails.all().values_list('user__email', flat=True)
		template = render_to_string('email_template.html', {'name':request.user.username, 'ataques':ataques_criticos})
		email = EmailMessage(
			'Amenazas Criticas Detectadas',
			template,
			settings.EMAIL_HOST_USER,
			[lista_emails],
		)

		email.fail_silently=False
		email.send()

		for alerta in lista_alertas:
			alerta.correo_enviado='t'
			alerta.save()

	context = {'empresa':empresa}
	return render(request, 'home.html', context)

#Pagina de detections################################################################################
@login_required(login_url='login')
@client_only
def Detections(request):
	empresa = Perfil.objects.get(user=request.user)
	empresa = empresa.empresa
	alertas = Alerta.objects.filter(usuario__empresa=empresa)
	

	context = {'alertas':alertas, 'empresa':empresa}

	return render(request, 'detections.html', context)


#Página de reportes #################################################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['cliente', 'user'])
def reportes(request):
	empresa = Perfil.objects.get(user=request.user)
	empresa = empresa.empresa
	alertas = Alerta.objects.filter(usuario__empresa=empresa)

	context = {'alertas':alertas, 'empresa':empresa}

	return render(request, 'reportes.html', context)




############################################################################
###############PÁGINAS DE GESTIÓN DE USUARIOS###############################
############################################################################
@login_required(login_url='login')
@admin_only
def GestionAdmin(request):
	listado_usuarios = User.objects.all()
	listado_usuarios = listado_usuarios.exclude(id=request.user.id)
	context = {'usuarios':listado_usuarios}
	return render(request, 'usersettings.html', context)

@login_required(login_url='login')
@client_only
def GestionCliente(request):
	empresa = Perfil.objects.get(user=request.user)
	empresa = empresa.empresa

	listado_perfiles = Perfil.objects.filter(empresa=empresa)
	listado_usuarios = []

	for perfil in listado_perfiles:
		id_user = perfil.user_id
		user = User.objects.get(id=id_user)
		listado_usuarios.append(user)

	context = {'empresa':empresa, 'usuarios':listado_usuarios}
	return render(request, 'gestion_cliente.html', context)


#####Eliminar usuarios##################################
@login_required
@admin_only
def deleteUser(request, id):
	user = User.objects.get(id=id)
	if request.method == 'POST':
		user.delete()
		messages.success(request, 'Usuario '+user.username+' eliminado con exito')
		return redirect('gestion_admin')

	return render(request, 'eliminar_usuario.html',{'user':user})

@login_required
@client_only
def deleteUserCliente(request, id):
	user = User.objects.get(id=id)

	empresa_req = Perfil.objects.get(user_id=request.user)
	empresa_req = empresa_req.empresa

	empresa_user = Perfil.objects.get(user_id=id)
	empresa_user = empresa_user.empresa

	if empresa_req != empresa_user:
		return redirect('gestion_cliente')

	if request.method == 'POST':
		user.delete()
		messages.success(request, 'Usuario '+user.username+' eliminado con exito')
		return redirect('gestion_cliente')

	context = {'empresa': empresa_req, 'usuario':user}
	return render(request, 'eliminar_usuario_cliente.html',context)


#############################################################################
#############################################################################
#############################################################################


#####Páginas de registro#############################################################################
##################################################################################################
##################################################################################################
#Registro de empresas y usuarios#
@login_required(login_url='login')
@admin_only
def AdminRegisterPage(request):
		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')
				group = Group.objects.get(name='cliente')
				user.groups.add(group)
				messages.success(request, 'Usuario '+username+' creado con exito')
				return redirect('gestion_admin')

		context = {'form':form}
		return render(request, 'register.html', context)

#subir usuarios con csv
@login_required
@admin_only
def subir_usuarios(request):
	template = "subir_usuarios.html"
	promt = {
		'orden': 'El orden del CSV debería ser: password, username, email'
	}

	if request.method == "GET":
		return render(request, template, promt)
	csv_file = request.FILES['file']
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'el archivo no es csv')

	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		password = column[0]
		username = column[1]
		email = column[2]
		_, nuevo_usuario = User.objects.update_or_create(
				username = username,
				password = password,
				email = email
			)
	
	context = {}
	return render(request, template, context)


@login_required(login_url='login')
@admin_only
def AsignarEmpresa(request,id):
		form = AsignarEmpresaForm()
		user = User.objects.get(id=id)
		if request.method == 'POST':
			form = AsignarEmpresaForm(request.POST)
			if form.is_valid():
				empresa = form.cleaned_data.get('empresa')
				perfil = Perfil(user=user,empresa=empresa)
				perfil.save()
				return redirect('home')

		context = {'form':form}
		return render(request, 'asignar_empresa.html', context)

@login_required(login_url='login')
@client_only
def ClientRegisterPage(request):
		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')
				group = Group.objects.get(name='user')
				user.groups.add(group)
				empresa = Perfil.objects.get(user=request.user)
				perfil = Perfil(user = user, empresa= empresa.empresa)
				perfil.save()
				messages.success(request, 'Usuario '+username+' creado con exito')
				return redirect('home')

		context = {'form':form}
		return render(request, 'registro_cliente.html', context)

##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################


#Pagina del Login
@unauthenticated_user
def loginPage(request):
		if request.method=='POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Credenciales incorrectas')

		context = {}
		return render(request, 'login.html', context)

#Vista del logout
def logoutUser(request):
	logout(request)
	return redirect('login')



#######################################################################
###################################GENERAR INFORMES PDF ###############
#######################################################################
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None



#vista previa del pdf

class pdfVistaPrevia(View):
	def get(self, request, *args, **kwargs):
		empresa = Perfil.objects.get(user=request.user)
		empresa = empresa.empresa
		alertas = Alerta.objects.filter(usuario__empresa=empresa)

		data = {'alertas':alertas}

		pdf = render_to_pdf('pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')

#Descargar PDF

class DescargarPDF(View):
	def get(self, request, *args, **kwargs):

		empresa = Perfil.objects.get(user=request.user)
		empresa = empresa.empresa
		alertas = Alerta.objects.filter(usuario__empresa=empresa)

		data = {'alertas':alertas}
		pdf = render_to_pdf('pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "INFORME DIF_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response		

#######################################################################



#Para recibir un JSON con los datos###########################################################################################
class GetChartsData(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):

		req_user = request.user
		
		req_user = req_user.id
	
		empresa = Perfil.objects.get(user__id=req_user)
		empresa = empresa.empresa
	
		lista_alertas = Alerta.objects.filter(usuario__empresa = empresa)
		

		labels_alertas = []
		labels_list = []
		data_alertas = []

		for alerta in lista_alertas:
			labels_list.append(alerta.tipo)
			if alerta.tipo not in labels_alertas:
				labels_alertas.append(alerta.tipo)

		for label in labels_alertas:
			repeticiones = labels_list.count(label)
			data_alertas.append(repeticiones)
			

		data = {
			"labels": labels_alertas,
			"data": data_alertas,
		}
		
		return Response(data)
