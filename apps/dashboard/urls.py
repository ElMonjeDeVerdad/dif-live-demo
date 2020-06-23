from django.urls import path, include
from .views import Dashboard, loginPage, AdminRegisterPage, ClientRegisterPage, logoutUser, Detections, AsignarEmpresa, GetChartsData, GestionAdmin, GestionCliente, reportes, deleteUser, deleteUserCliente, pdfVistaPrevia, DescargarPDF, subir_usuarios, ComprarDIFTemplate


urlpatterns = [
	path('home/', Dashboard, name="home"), #HOME
	path('comprar/', ComprarDIFTemplate, name="comprar"), #COMPRAR DIF
	path('detections/', Detections, name="detections"), #DETECCIONES
	path('reportes/', reportes, name="reportes"), #REPORTES
	path('gestion_admin/', GestionAdmin, name="gestion_admin"), #GESTIÓN ADMIN
	path('gestion_cliente/', GestionCliente, name="gestion_cliente"), #GESTIÓN CLIENTE
	path('', loginPage, name="login"), #LOGIN
	path('registro_admin/', AdminRegisterPage, name="register"), #REGISTRO ADMIN
	path('asignar_empresa/<str:id>', AsignarEmpresa, name="asignar_empresa"), #ASIGNAR EMPRESA
	path('eliminar_usuario/<str:id>', deleteUser, name="eliminar_usuario"), #ELIMINAR USUARIO
	path('eliminar_usuario_cliente/<str:id>', deleteUserCliente, name="eliminar_usuario_cliente"), #ELIMINAR USUARIO
	path('registro_cliente/', ClientRegisterPage, name="register_cliente"), #REGISTRO CLIENTE
	path('logout/', logoutUser, name="logout"), #LOGOUT
	path('data/', GetChartsData.as_view(), name="data"), #CHARTS DATA
	path('pdf_vista_previa/', pdfVistaPrevia.as_view(), name="ver_pdf"), #VER PDF
	path('pdf_descargar/', DescargarPDF.as_view(), name="descargar_pdf"), #DESCARGAR PDF
	path('subir_csv/', subir_usuarios, name="subir_usuarios"), #SUBIR USUARIOS
]