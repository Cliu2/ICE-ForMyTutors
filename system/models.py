from django.db import models

# Create your models here.
class Instructor(models.Model):
	name=models.CharField(max_length=200)
	UID=models.CharField(max_length=200)
	#pwd will be handled by Django, so not included
	email=models.EmailField()
	autobiagraphy=models.TextField()
	def __str__(self):
		return f'{self.name} ({self.autobiagraphy})'