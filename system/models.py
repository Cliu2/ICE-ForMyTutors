from django.db import models

# Create your models here.
class Instructor(models.Model):
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	username=models.CharField(max_length=200)
	encodedPW=models.CharField(max_length=200)
	#pwd will be handled by Django, so not included
	email=models.EmailField()
	autobiagraphy=models.TextField()
	def __str__(self):
		return f'{self.name} {self.lastname} ({self.autobiagraphy})'
