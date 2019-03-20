from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views.generic.list import ListView

# Create your views here.

"""
	both users
"""
def showCourses(request, **kwargs):
	user_id = kwargs['user_id']
	users = Instructor.objects.get(id=user_id)
	if len(users)==0:
		type = 'learner'
		user = Learner.objects.get(id=user_id)[0]
		course_list = Enroll.objects.get(learner__id=user_id).values('course')
	else:
		user = users[0]
		type = 'instructor'
		course_list = Course.objects.get(instructor__id=user_id)
	context = {
		'course_list': course_list,
		'type': type
	}
	return HttpResponse(template.render(context, request))


def showModules(request, **kwargs):
	u_id = kwargs['user_id']
	c_id = kwargs['course_id']
	users = Instructor.objects.get(id=user_id)
	if len(users)==0:
		type = 'learner'
		#user = Learner.objects.get(id=user_id)[0]
		course = Enroll.objects.get(learner_id=u_id, course_id=c_id).values('course')[0]
	else:
		type = 'instructor'
		course = Course.objects.get(instructor__id=user_id)[0]
	context = {
		'course': course,
		'type': type
	}

def showComponents(request, **kwargs):
	pass

"""
	instructor manage course
"""

def manageModule(request, **kwargs):
	pass
def manageComponent(request, **kwargs):
	pass
def showQuizzes(request, **kwargs):
	pass
def viewQuiz(request, **kwargs):
	pass

"""
	learner study course
"""
def takeQuiz(request, **kwargs):
	pass

"""
	instructor views
"""
class ManageModule(ListView):
	model=Module
	template_name='manageModule.html'

class ShowComponents(ListView):
	model=ComponentText
	template_name='component.html'

class ShowCourses(ListView):
	model = Course
	template_name = 'courseList.html'

class showQuiz(ListView):
	"""To be Done"""
	pass


"""
	learner views

def showCourses(request, learner_id):			# course list for a learner
	l_courses = Enroll.objects.get(learner__id=learner_id).values('course')
	template = loader.get_template("course_list.html")
	context = {
		'l_courses': l_courses
	}
	return HttpResponse(template.render(context, request))

def viewCourse(request, learner_id, course_id):
	c_modules = Module.objects.get(course__id=course_id)
	l_progress = Enroll.objects.get(course__id=course_id, learner__id=learner_id).values('progress')
	template = loader.get_template("course_content.html")
	context = {
		'c_modules': c_modules,
		'l_progress': l_progress
	}
	return HttpResponse(template.render(context, request))

def studyModule(request,**kwargs):
	# to be done
	pass

def takeQuiz(request,**kwargs):
	#to be done
	pass
"""
