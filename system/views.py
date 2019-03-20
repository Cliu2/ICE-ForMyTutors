from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views.generic.list import ListView

# Create your views here.
class ManageModule(ListView):
	model=Module
	template_name='manageModule.html'

class showComponent(ListView):
	model=ComponentText
	template_name='component.html'

class ShowCourse(ListView):
	model = Course
	template_name = 'courseList.html'

class showQuiz(ListView):
	"""To be Done"""
	pass


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
