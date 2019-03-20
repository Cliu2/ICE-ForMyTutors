from django.db import models

class Instructor(models.User):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	autobiagraphy=models.TextField()
	def __str__(self):
		return f'{self.user.first_name} {self.user.last_name} ({self.autobiagraphy})'

class Learner(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	staffID = models.CharField(max_length=8)
	def __str__(self):
		return f'{self.user.username}'

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
	lmt = models.DateField(initial=datetime.date.today)

class Component(models.Model):
	#order=models.IntegerField()
	#title=models.CharField(max_length=200)
	course=models.ForeignKey(Course,on_delete=models.CASCADE)
	#module=models.ForeignKey(Module,null=True, blank=True,on_delete=models.SET_NULL)

class ComponentText(Component):
	component = ForeignKey(Component, on_delete=models.CASCADE)
	content=models.TextField()

class ComponentImage(Component):
	component = ForeignKey(Component, on_delete=models.CASCADE)
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

class Component_in_Module(models.Model):
	component = models.ForeignKey(Component, on_delete=models.CASCADE)
	module = models.ForeignKey(Module, on_delete=models.CASCADE)
	order = models.IntegerField()

# class Question_in_Quiz(models.Model):
# 	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
# 	question = models.ForeignKey(Question, on_delete=models.CASCADE)
