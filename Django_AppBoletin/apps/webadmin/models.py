from django.db import models

# Create your models here.

class BoletinModelo(models.Model):
	titulo = models.CharField(max_length=50)
	resumen = models.CharField(max_length=250)
	detalle = models.TextField()
	fecha = models.DateField(max_length=10)
	TIPOS = (('N','Noticias'),('E','Eventos'))
	tipo = models.CharField(max_length=1,choices=TIPOS,default='N')

	def __str__(self):
		return self.titulo

