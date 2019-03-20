from django.db import models

class Instructor(models.Model):

	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	username=models.CharField(max_length=200)
	# encodedPW=models.CharField(max_length=200)

	#pwd will be handled by Django, so not included
	autobiagraphy=models.TextField()
	def __str__(self):
		return f'{self.firstname} {self.lastname} ({self.autobiagraphy})'

class Learner(models.Model):
	staffID = models.CharField(max_length=8)
	username = models.CharField(max_length=200)
	email = models.EmailField()
	# pwd = models.CharField(max_length=16)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)

class Course(models.Model):
	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField()
	CECU = models.IntegerField()
	category = models.CharField(max_length=100)
	status = models.BooleanField(default=False)

class Module(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	order=models.IntegerField()
	title=models.CharField(max_length=200)

class Component(models.Model):
	order=models.IntegerField()
	title=models.CharField(max_length=200)
	course=models.ForeignKey(Course,on_delete=models.CASCADE)
	module=models.ForeignKey(Module,null=True, blank=True,on_delete=models.SET_NULL)

class ComponentText(Component):
	content=models.TextField()

class ComponentImage(Component):
	content=models.ImageField()

class Quiz(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	module=models.ForeignKey(Module,null=True,blank=True,on_delete=models.SET_NULL)
	pass_score = models.IntegerField()

class Question(models.Model):
	description = models.TextField()
	option_1 = models.TextField()
	option_2 = models.TextField()
	option_3 = models.TextField()
	option_4 = models.TextField()
	answer = models.CharField(max_length=1)
	module=models.ForeignKey(Module,on_delete=models.CASCADE)

"""
	???
"""
class Enroll(models.Model):
	learner = models.ForeignKey(Course, on_delete=models.CASCADE)
	course = models.ForeignKey(Learner, on_delete=models.CASCADE)
	status = models.BooleanField()
	progress = models.IntegerField()								# modules that visible to the learner


# class Question_in_Quiz(models.Model):
# 	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
# 	question = models.ForeignKey(Question, on_delete=models.CASCADE)
