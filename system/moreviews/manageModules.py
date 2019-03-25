import sys
sys.path.append("..")
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views import View
from ..forms import *
from ..models import *

def selectComponent(request,**kwargs):
	course_id=kwargs['course_id']
	module_id=kwargs['module_id']
	course=Course.objects.get(id=course_id)
	module=Module.objects.get(id=module_id)
	all_components=Component.objects.filter(course__id=course_id, module__isnull=True)

	template=loader.get_template("showComponent.html")
	context={'components':all_components,
			 'module':module,
			 'course':course,
			 'instructor_id':kwargs['instructor_id']}
	return HttpResponse(template.render(context,request))


def addComponent(request,**kwargs):
	course=Course.objects.get(id=kwargs['course_id'])
	module_id=kwargs['module_id']
	component_id=kwargs['component_id']
	component=Component.objects.get(id=component_id)
	module=Module.objects.get(id=module_id)
	index=len(Component.objects.filter(module__id=module_id))
	component.module=module
	component.setOrder(index)
	component.save()

	all_text_components=ComponentText.objects.filter(module__id=module_id)
	all_image_components=ComponentImage.objects.filter(module__id=module_id)
	quiz=Quiz.objects.filter(module__id=module_id)
	all_components=[]
	for t in all_text_components:
		t.istext=True
		all_components.append(t)
	for i in all_image_components:
		i.isimage=True
		all_components.append(i)

	


	template=loader.get_template("moduleContent.html")
	context={'components':all_components,
			 'quiz':quiz,
			 'instructor_id':kwargs['instructor_id'],
			 'course':course,
			 'module':module
			 }
	return HttpResponse(template.render(context,request))