from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views.generic.list import ListView

# Create your views here.

"""
	both users
"""

def viewEnrolled(request, **kwargs):
	# 	
	#	Design Model 1: viewEnrolled(user_id)
	# 	type: determines learner page/instructor page
	# 	course_list: query course object enrolled by user/created by instructor, ordered by status
	# 	status: query object might determine display or not, or the order to display 
	# 	user: the user exactly
	# 
	user_id = kwargs['user_id']
	users = Instructor.objects.filter(id=user_id)
	template = loader.get_template("course_list.html")
	if len(users)==0:
		users = Learner.objects.filter(id=user_id)
		type = 'learner'
		course_id_list = Enrolment.objects.filter(learner__id=user_id).order_by('status').values('course')
		courses = []
		for course in course_id_list:
			courses.append(Course.objects.filter(id = course['course'])[0])
		status = Enrolment.objects.filter(learner__id=user_id).values('status')

	else:
		user = users[0]
		type = 'instructor'
		courses = Course.objects.filter(instructor__id=user_id).order_by('status')
		status = Enrolment.objects.filter(learner__id=user_id).values('status')
	context = {
		'user': users,
		'course_list': courses,
		'type': type,
		'status': status,

	}
	return HttpResponse(template.render(context, request))


def viewCourse(request, **kwargs):
	# 
	# 	type: determines learner page/ instructor page
	# 	course: a certain course enrolled by user/created by instructor that has entered
	# 	modules: with the 'order' attribute to determine the order of display
	# 	progress: start with 0? then progress = -1 for instructor as a dumplicate attribute, control the access of modules
	# 
	u_id = kwargs['user_id']
	c_id = kwargs['course_id']
	template = loader.get_template("courseContent.html")
	users = Instructor.objects.filter(id=u_id)
	course = Course.objects.filter(id=c_id)[0]
	if len(users)==0:
		type = 'learner'
		modules = Module.objects.filter(course__id=c_id).order_by('order')
		progress = Enrolment.objects.filter(learner_id=u_id, course_id=c_id).values('progress')[0]['progress']
	else:
		type = 'instructor'
		modules = Module.objects.filter(course__id=c_id).order_by('order')
		progress = -1
	context = {
		'course': course,
		'modules': modules,
		'type': type,
		'progress': progress,
	}
	return HttpResponse(template.render(context, request))

def viewModule(request, **kwargs):
	# 
	# 	components: a query component object in a certain module ordered by order attribute
	# 
	u_id = kwargs['user_id']
	c_id = kwargs['course_id']
	m_id = kwargs['module_id']
	template =loader.get_template("moduleContent.html")
	module = Module.objects.filter(id= m_id)[0]
	users = Instructor.objects.filter(id=u_id)  
	components = Component.objects.filter(module__id=m_id).order_by('order')
	componentURL = components
	if len(users) == 0:
		type = 'learner'
		progress = Enrolment.objects.filter(learner_id=u_id, course_id=c_id).values('progress')[0]['progress']
	else:
		type = 'instructor'
		progress = -1
	context = {
		'type': type,
		'components': components,
		'module': module,
		'progress': progress,
	}
	return HttpResponse(template.render(context, request))


def takeQuiz(request, **kwargs):
	m_id = kwargs['module_id']
	template =loader.get_template("takeQuiz.html")
	quiz = Quiz.objects.filter(module__id = m_id)[0]
	q_id = quiz.pk
	question_list = Question.objects.filter(quiz__id = q_id).order_by('?')[:(quiz.num_to_draw)]
	context = {
		'question_list': question_list,
	}
	return HttpResponse(template.render(context, request))

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def submitAnswer(request, **kwargs):
	c_id = kwargs['course_id']
	m_id = kwargs['module_id']
	u_id = kwargs['user_id']
	res = request.GET
	template =loader.get_template("submitAnswer.html")
	quiz = Quiz.objects.filter(module__id = m_id)[0]
	submitted = {x: res[x] for x in res if RepresentsInt(x)}
	count = 0
	for x in submitted:
		if submitted[x] == res["q"+x]:
			count+=1
	count=count*100/quiz.num_to_draw
	if count >= quiz.pass_score:
		passing = "pass"
		prog =  Enrolment.objects.filter(learner_id=u_id, course_id=c_id).values('progress')[0]['progress']
		Enrolment.objects.filter(learner__id = u_id,course__id = c_id).update(progress=prog+1)
	else:
		passing = "fail"
	context = {
		'submitted':submitted,
		'pass':passing,
	}
	return HttpResponse(template.render(context, request))
"""
	instructor manage course
"""

def manageModule(request, **kwargs):
	u_id = kwargs['instructor_id']
	c_id = kwargs['course_id']
	modules = Module.objects.filter(course__id=c_id).order_by('order')
	template = loader.get_template("manageModule.html")
	context = {
		'modules': modules,
	}
	return HttpResponse(template.render(context, request))


def selectComponent(request, **kwargs):
	pass
def addComponent(request, **kwargs):
	pass
def selectQuiz(request, **kwargs):
	pass
def addQuiz(request, **kwargs):
	pass

