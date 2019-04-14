import sys
sys.path.append("..")
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views import View
from django.core.exceptions import SuspiciousOperation
from ..forms import *
from ..models import *

def loadHome(request,**kwargs):
	user=request.user
	if isinstance(user,Instructor):
		print("instructor!")

	elif isinstance(user,Learner):
		print("learner!")
	return redirect('/system/view/{}/'.format(user.pk))
	template=loader.get_template("loadHome.html")
	context={}
	return HttpResponse(HttpResponse(template.render(context,request)))