from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.generic import TemplateView
from .models import *
from django.views.generic.list import ListView
from django.views import View
from .forms import *
from .moreviews import manageModules
from django.core.exceptions import SuspiciousOperation
import itertools

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
		course_list = list(enroll.course for enroll in Enroll.objects.filter(learner__id=user_id).order_by('status'))
		status = list(enroll.status for enroll in Enroll.objects.filter(learner__id=user_id).order_by('status'))

	else:
		user = users[0]
		type = 'instructor'
		course_list = list(Course.objects.filter(instructor__id=user_id).order_by('status'))
		status = list(c.status for c in Course.objects.filter(instructor__id=user_id).order_by('status'))
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
		course = Course.objects.filter(id=c_id)[0]
		modules = Module.objects.filter(course__id=c_id).order_by('order')
		progress = Enroll.objects.filter(learner_id=u_id, course_id=c_id).values('progress')[0]['progress']

	else:
		type = 'instructor'
		course = Course.objects.filter(id=c_id)[0]
		if course.instructor.pk!=u_id:
			raise SuspiciousOperation("Course does not belong to current instructor!")
		modules = Module.objects.filter(course__id=c_id).order_by('order')
		progress = -1
	context = {
		'course': course,
		'modules': modules,
		'type': type,
		'progress': progress,
		'u_id': u_id,
	}
	return HttpResponse(template.render(context, request))


"""
def ICourseList(request, **kwargs):
	instructor = Instructor.objects.filter(id=kwargs['instructor_id'])[0]
	course_list = list(Course.objects.filter(instructor__id=user_id).order_by('status'))
	status = list(c.status for c in Course.objects.filter(instructor__id=user_id).order_by('status'))
	context = {
		'course_list': course_list,
		'status': status,
		'insturctor': instructor,
	}
	return HttpResponse(template.render())
"""

def addModule(request, **kwargs):
	title = request.GET.get('title', None)
	course = Course.objects.filter(id=request.GET.get('c_id', None))[0]
	if len(Module.objects.filter(course__id=course.id))==0:
		order = 0
	else:
		order = Module.objects.filter(course__id=course.id).order_by('-order').values('order')[0]['order']
	module = Module(course=course, order=order, title=title)
	module.save()
	return redirect('/system/view/{}/{}/'.format(request.GET.get('i_id', None), course.id))

def addCourse(request, **kwargs):
	title = request.GET.get('title', None)
	description = request.GET.get('description', None)
	category = Category.objects.filter(name=request.GET.get('category', None))[0]
	CECU = request.GET.get('CECU', None)
	instructor = Instructor.objects.filter(id=kwargs['instructor_id'])[0]
	course = Course(instructor=instructor,
					category=category,
					title=title,
					description=description,
					CECU_value=CECU,
					status=1)
	course.save()
	return redirect('/system/view/{}/'.format(kwargs['instructor_id']))

def deleteModule(request, **kwargs):
	template = loader.get_template("showModules.html")
	Module.objects.filter(id=kwargs['module_id']).delete()
	modules = Module.objects.filter(course__id=kwargs['course_id']).order_by('order')
	return redirect('/system/view/{}/{}/'.format(kwargs['instructor_id'], kwargs['course_id']))

def removeQuiz(request, **kwargs):
	quiz = Quiz.objects.get(id=kwargs['quiz_id'])
	quiz.module = None
	quiz.save()
	components = Component.objects.filter(module__id=kwargs['module_id']).order_by('order')
	return redirect('/system/manage/{}/{}/{}/displayModuleContent/'.format(kwargs['instructor_id'],
																			kwargs['course_id'],
																			kwargs['module_id']))

def showQuizzes(request, **kwargs):
	has_quiz = Quiz.objects.filter(module__id=kwargs['module_id'])
	if(len(has_quiz)==0):
		all_quizzes = Quiz.objects.filter(course__id=kwargs['course_id'], module=None)
		template = loader.get_template("showQuizzes.html")
		context = {
			'course': Course.objects.filter(id=kwargs['course_id'])[0],
			'course_id': kwargs['course_id'],
			'module': Module.objects.filter(id=kwargs['module_id'])[0],
			'module_id': kwargs['module_id'],
			'instructor_id': kwargs['instructor_id'],
			'all_quizzes':all_quizzes,
		}
		return HttpResponse(template.render(context, request))
	else:
		return manageModules.displayModuleContent(request, module_id=kwargs['module_id'], course_id=kwargs['course_id'], instructor_id=kwargs['instructor_id'])


# 'manage/<int:instructor_id>/<int:course_id>/<int:module_id>/addQuiz/<int:quiz_id>/'
def addQuiz(request, **kwargs):
	quiz = Quiz.objects.filter(id=kwargs['quiz_id'])[0]
	module = Module.objects.filter(id=kwargs['module_id'])[0]
	quiz.module = module
	quiz.save()

	return redirect('/system/manage/{}/{}/{}/displayModuleContent/'.format(kwargs['instructor_id'],
																		   kwargs['course_id'],
																		   kwargs['module_id']))
