from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Instructor(User):												# an instructor object has no id attribute before save()
	autobiagraphy=models.TextField()
	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class Learner(User):
	staffID = models.CharField(max_length=8)
	cumCECU = models.IntegerField()
	def __str__(self):
		return f'{self.username}\n'

class Course(models.Model):
	STATUS = (
		(0,'Open'),
		(1,'Pending'),
		(2,'Closed'),
	)
	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField()
	CECU = models.IntegerField()
	category = models.CharField(max_length=100)
	status = models.IntegerField(choices=STATUS)
	def __str__(self):
		return f'Instructor: {self.instructor.first_name} {self.instructor.last_name} | Title: {self.title}\n'
	def setModuleAccess(self, progress):
		pass
	def updateProgress(self, progress):
		pass


class Module(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	order = models.IntegerField()
	title=models.CharField(max_length=200)
	lmt = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return f'Course: {self.course.title} | Title: {self.title}'
	def takeQuiz(self):
		pass
	def setOrder(self,order):
		self.order = order


class Component(models.Model):
	order=models.IntegerField(default=-1)
	title=models.CharField(max_length=200, blank=True)			# title of component?
	course=models.ForeignKey(Course,on_delete=models.CASCADE)
	module=models.ForeignKey(Module, default=None, null=True, blank=True, on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def setOrder(self,order):
		self.order = order


class ComponentImage(Component):
	path=models.CharField(max_length=200)

class ComponentText(Component):
	content=models.TextField()

class Quiz(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	module=models.ForeignKey(Module,null=True,blank=True,on_delete=models.SET_NULL)
	pass_score = models.IntegerField()
	num_to_draw = models.IntegerField()
	def drawQuestions(self):
		pass
	def getResult(self,ans):
		pass

class Question(models.Model):
	description = models.TextField()
	option_1 = models.TextField()
	option_2 = models.TextField()
	option_3 = models.TextField()
	option_4 = models.TextField()
	answer = models.CharField(max_length=1)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	def checkAnswer(self, ans):
		return (ans == self.answer)


class Enrolment(models.Model):
	learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	status = models.BooleanField()
	progress = models.IntegerField()								# modules that visible to the learner
	finish_time = models.DateField(default=None)
	def __str__(self):
		return f'{self.learner} | {self.course.title}'
	def awardCECU(self):
		pass
	def setProgress(self,progress):
		self.progress = progress
