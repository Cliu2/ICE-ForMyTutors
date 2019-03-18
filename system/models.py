from django.db import models

class Instructor(models.Model):
	"""
	UID=models.CharField(max_length=200)		# automatically generated primary key
	"""
	uname = models.CharField(max_length=200)
	email = models.EmailField()
	pwd = models.CharField(max_length=16)
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)

	#pwd will be handled by Django, so not included
	autobiagraphy=models.TextField()
	def __str__(self):
		return f'{self.name} ({self.autobiagraphy})'

class Learner(models.Model):
	staffID = models.CharField(max_length=8)
	uname = models.CharField(max_length=200)
	email = models.EmailField()
	pwd = models.CharField(max_length=16)
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)

class Course(models.Model):
	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField()
	CECU = models.IntegerFieled()
	category = models.CharField(max_length=100)
	status = models.BooleanField(default=False)

class Module(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Quiz(models.Model):
	course = models.ForeignKey(Course. on_delete=models.CASCADE)
	pass_score = models.IntegerFieled()

class Question(models.Model):
	description = models.TextField()
	option_1 = models.TextField()
	option_2 = models.TextField()
	option_3 = models.TextField()
	option_4 = models.TextField()
	answer = models.CharField(max_length=1)


"""
	???
"""
class Take(models.Model):
	learner = models.ForeignKey(Course, on_delete=models.CASCADE)
	course = models.ForeignKey(Learner, on_delete=models.CASCADE)

class Component_in_Module(models.Model):
	pass

class Question_in_Quiz(models.Model):
	quiz = models.ForeignKey(Quiz)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
