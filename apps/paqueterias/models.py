from django.db import models
from apps.responsables.models import Responsable

# Create your models here.
class Paqueteria(models.Model):
	name_paq = models.CharField(max_length=255)
	logo = models.ImageField(upload_to='logos')
	responsable = models.ForeignKey(Responsable)

	def __unicode__(self):
		return self.name_paq