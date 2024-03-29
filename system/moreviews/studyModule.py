import sys
sys.path.append("..")
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from system.models import *
from django.views.generic.list import ListView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

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
		# [{'course':1},{'course':3},{'course':4}] -> course model list
		courses = []
		for course in course_id_list:
			courses.append(Course.objects.filter(id = course['course'])[0])
		status = Enrolment.objects.filter(learner__id=user_id).values('status')

	else:
		type = 'instructor'
		courses = Course.objects.filter(instructor__id=user_id).order_by('status')
		status = 0
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
	u_id = request.user.id
	c_id = kwargs['course_id']
	m_id = kwargs['module_id']
	template =loader.get_template("learnerModuleContent.html")
	module = Module.objects.filter(id= m_id)[0]
	users = Instructor.objects.filter(id=u_id)
	all_text_components=ComponentText.objects.filter(module__id=m_id)
	all_image_components=ComponentImage.objects.filter(module__id=m_id)
	all_components=[None for i in range(len(all_text_components)+len(all_image_components))]
	for t in all_text_components:
		t.istext=True
		all_components[t.order]=t
	for i in all_image_components:
		i.isimage=True
		all_components[i.order]=i
	if len(users) == 0:
		type = 'learner'
		progress = Enroll.objects.filter(learner_id=u_id, course_id=c_id).values('progress')[0]['progress']
	else:
		type = 'instructor'
		progress = -1
	context = {
		'type': type,
		'components': all_components,
		'module': module,
		'progress': progress,
	}
	return HttpResponse(template.render(context, request))


def takeQuiz(request, **kwargs):
	m_id = kwargs['module_id']
	template =loader.get_template("takeQuiz.html")
	quiz = Quiz.objects.filter(module__id = m_id)[0]
	q_id = quiz.pk
	question_list = Question.objects.filter(quiz__id = q_id).order_by('?')[:(quiz.num_draw)]
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
	u_id = request.user.id
	res = request.GET
	template =loader.get_template("submitAnswer.html")
	quiz = Quiz.objects.filter(module__id = m_id)[0]
	submitted = {x: res[x] for x in res if RepresentsInt(x)}
	count = 0
	for x in submitted:
		if submitted[x] == res["q"+x]:
			count+=1
	if count >= quiz.pass_score:
		passing = "pass"
		enroll = Enroll.objects.filter(learner__id=u_id, course__id=c_id)[0]
		old_prog = enroll.progress
		new_prog = old_prog + 1
		num_of_modules = Module.objects.filter(course__id=c_id).count()
		if enroll.progress < num_of_modules:
			enroll.progress = new_prog
			enroll.save()
		if new_prog >= num_of_modules:
			enroll.awardCECU()
			sendPassEmail(request.user, enroll.course)

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
def modiModuleOrd(request,**kwargs):
	c_id = kwargs['course_id']
	m_id = kwargs['module_id']
	template =loader.get_template("modiModuleOrd.html")
	modules = Module.objects.filter(course__id=c_id).order_by('order')
	module = Module.objects.filter(id=m_id)[0]
	ex_module = modules.exclude(id=m_id)
	largest_order_mod=ex_module.order_by('-order')[0]
	context = {
		'ex_module': ex_module,
		'modules': largest_order_mod,
		'module' : module,
	}
	return HttpResponse(template.render(context, request))

def moduleOrder(request,**kwargs):
	res = request.GET
	c_id = kwargs['course_id']
	template =loader.get_template("moduleOrder.html")
	modules = Module.objects.filter(course__id=c_id).order_by('order')
	moduleList = []
	if res['choice'] == 'last':
		for module in modules:
			if module.id != int(res['exclu']):
				moduleList.append(module.id)
			moduleList.append(int(res['exclu']))
	else:
		for module in modules:
			if module.id != int(res['exclu']):
				if module.id == int(res['choice']):
					moduleList.append(int(res['exclu']))
				moduleList.append(module.id)
	for i ,m in enumerate(moduleList):
		Module.objects.filter(id = m).update(order = i)
	context = {
	}
	return HttpResponse(template.render(context, request))

def modiCompOrd(request, **kwargs):
	m_id = kwargs['module_id']
	comp_id = kwargs['component_id']
	template =loader.get_template("modiCompOrd.html")
	components = Component.objects.filter(module__id=m_id).order_by('order')
	component = Component.objects.filter(id=comp_id)[0]
	ex_component = components.exclude(id=comp_id)
	largest_order_comp=ex_component.order_by('-order')[0]
	context = {
		'ex_component': ex_component,
		'components': largest_order_comp,
		'component' : component,
	}
	return HttpResponse(template.render(context, request))





def compOrder(request, **kwargs):
	res = request.GET
	m_id = kwargs['module_id']
	template =loader.get_template("compOrder.html")
	components = Component.objects.filter(module__id=m_id).order_by('order')
	compList = []
	if res['choice'] == 'last':
		for component in components:
			if component.id != int(res['exclu']):
				compList.append(component.id)
			compList.append(int(res['exclu']))
	else:
		for component in components:
			if component.id != int(res['exclu']):
				if component.id == int(res['choice']):
					compList.append(int(res['exclu']))
				compList.append(component.id)
	for i ,c in enumerate(compList):
		Component.objects.filter(id = c).update(order = i)
	context = {
	}
	return HttpResponse(template.render(context, request))


def browseCourse(request, **kwargs):
	template = loader.get_template('showAvailableCourses.html')
	enrollments = Enroll.objects.filter(learner__id=request.user.id)
	open_courses = Course.objects.filter(status=0).order_by('title')
	context = {
		'course_list': open_courses,
		'learner': Learner.objects.filter(id=request.user.id)[0]
	}
	return HttpResponse(template.render(context, request))

def viewCourseHistory(request, **kwargs):
	template = loader.get_template('courseHistory.html')
	enrolls = list({'course': e.course, 'finish_time': e.finish_time} for e
    				in Enroll.objects.filter(learner__id=request.user.id, status=True).order_by('finish_time'))
	cummulative_CECU = sum(list(e.course.CECU_value for e in Enroll.objects.filter(learner_id=request.user.id, status=True)))
	context = {
		'enrolls': enrolls,
		'learner': Learner.objects.filter(id=request.user.id)[0],
		'cummulative_CECU': cummulative_CECU
	}
	return HttpResponse(template.render(context, request))

def sendPassEmail(user, course):
	mail_subject = 'Pass Course Notification'
	message = render_to_string('passConfirmation.html', {
								'name': user.username,
								'course': course
								})
	email = EmailMessage(mail_subject, message, to=[user.email])
	email.send()



def manageModule(request, **kwargs):
	pass


def selectComponent(request, **kwargs):
	pass
def addComponent(request, **kwargs):
	pass
def selectQuiz(request, **kwargs):
	pass
def addQuiz(request, **kwargs):
	pass
