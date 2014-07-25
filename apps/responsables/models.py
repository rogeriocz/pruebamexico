from django.db import models

# Create your models here.
class Responsable(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	comentario = models.TextField(blank=True)

	def __unicode__(self):
		return self.first_name