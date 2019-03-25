from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views.generic.list import ListView
from django.views import View

# Create your views here.

"""
	both users
"""

def showCourses(request, **kwargs):
	#
	# 	type: determines learner page/ instructor page
	# 	course_list: query course object enrolled by user/created by instructor, not ordered
	# 	status: might determine display or not, or the order to display (currently a boolean object, to be changed to int)
	# 	user: the user exactly
	#
	user_id = kwargs['user_id']
	users = Instructor.objects.filter(id=user_id)
	template = loader.get_template("showCourses.html")
	if len(users)==0:
		type = 'learner'
		user = Learner.objects.filter(id=user_id)[0]
		course_list = Enroll.objects.filter(learner__id=user_id).values('course')
		status = Enroll.objects.filter(learner__id=user_id).values('status')[0]

	else:
		user = users[0]
		type = 'instructor'
		course_list = Course.objects.filter(instructor__id=user_id)
		status = course_list.values('status')[0]
	context = {
		'course_list': course_list,
		'type': type,
		'status': status,
		'user':user,
	}
	return HttpResponse(template.render(context, request))


def showModules(request, **kwargs):
	#
	# 	type: determines learner page/ instructor page
	# 	course: a certain course enrolled by user/created by instructor that has entered
	# 	modules: with the 'order' attribute to determine the order of display
	# 	progress: start with 0? then progress = -1 for instructor as a dumplicate attribute, control the access of modules
	#
	u_id = kwargs['user_id']
	c_id = kwargs['course_id']
	template = loader.get_template("showModules.html")
	users = Instructor.objects.filter(id=u_id)
	if len(users)==0:
		type = 'learner'
		course = Enroll.objects.filter(learner_id=u_id, course_id=c_id).values('course')[0]
		modules = Module.objects.filter(course__id=c_id).order_by('order')
		progress = Enroll.objects.filter(learner_id=u_id, course_id=c_id).values('progress')[0]
	else:
		type = 'instructor'
		course = Course.objects.filter(instructor__id=u_id)
		modules = Module.objects.filter(course__id=c_id).order_by('order')
		progress = -1
	context = {
		'course': course,
		'modules': modules,
		'type': type,
		'progress': progress,
	}
	return HttpResponse(template.render(context, request))
"""
def showComponents(request, **kwargs):
	#
	# 	components: a query component object in a certain module ordered by order attribute
	#
	#u_id = kwargs['user_id']
	#c_id = kwargs['course_id']
	m_id = kwargs['module_id']
	template =loader.get_template("showComponents.html")
	components = Component.objects.filter(module__id=m_id).values('component').order_by('order')
	context = {
		'components': components,
	}
	return HttpResponse(template.render(context, request))
"""



#	instructor manage course

"""
def enterModuleInfo(request, **kwargs):
	template = loader.get_template("enterModuleInfo.html")
	context = {
		'i_id': kwargs['instructor_id'],
		'c_id': kwargs['course_id'],
	}
	return HttpResponse(template.render(context, request))

class addModule(View):
	def post(self, request):
		course = Course.objects.filter(c_id=request.POST.get("c_id"))								# do not care order so far
		title = request.POST.get("title")
		new_module = Module(course=course, title=title)
		new_module.save()
		return showModules(user_id=request.POST.get("u_id"), course_id=request.POST.get("c_id"))
"""

"""
def manageComponent(request, **kwargs):
	pass
def showQuizzes(request, **kwargs):
	pass
def viewQuiz(request, **kwargs):
	pass


	#learner study course

def takeQuiz(request, **kwargs):
	pass

	#instructor views

class ManageModule(ListView):
	pass

class ShowComponents(ListView):
	pass

class ShowCourses(ListView):
	pass

class showQuiz(ListView):
	pass



	#learner views

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
