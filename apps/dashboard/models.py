from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#Empresas registradas en DIF
class Perfil(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	empresa = models.CharField(max_length=50, null=True)

#Alertas obtenidas por el NIDS
class Alerta(models.Model):
	CATEGORIA = (
		('3', '3'),
		('2', '2'),
		('1', '1'),
		)

	CHECKED = (
		('t', 't'),
		('f', 'f'),
		)

	ip_origen = models.CharField(max_length=30, null=True)
	ip_destino = models.CharField(max_length=30, null=True)
	puerto_origen = models.CharField(max_length=10, null=True)
	puerto_destino = models.CharField(max_length=30, null=True)
	fecha = models.DateField(null=True)
	riesgo = models.CharField(max_length=50, null=True, choices = CATEGORIA)
	tipo = models.CharField(max_length=20, null=True)
	mensaje = models.CharField(max_length=50, null=True)
	correo_enviado = models.CharField(max_length=3,default='f', choices=CHECKED)
	usuario = models.ForeignKey(Perfil, null=True, on_delete=models.CASCADE)