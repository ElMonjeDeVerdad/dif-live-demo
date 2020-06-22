from django.http import HttpResponse
from django.shortcuts import redirect


#si estas registrado no te deja entrar
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return redirect('gestion_admin')
		return wrapper_func
	return decorator


def admin_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group != 'admin':
			return redirect('home')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_func

def client_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group != 'cliente':
			return redirect('home')

		if group == 'cliente':
			return view_func(request, *args, **kwargs)

	return wrapper_func

def gestion_usuarios(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'admin':
			return view_func(request, *args, **kwargs)

		if group == 'cliente':
			return redirect('gestion_cliente')

		if group == 'user':
			return redirect('home')

	return wrapper_func
