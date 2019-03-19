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