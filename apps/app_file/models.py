from django.db import models

# Create your models here.
class App_file(models.Model):
	name = models.CharField(max_length=255)
	order = models.PositiveIntegerField()
	up_file = models.FileField(upload_to='archivos')