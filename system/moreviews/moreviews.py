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
import json

def loadCategory(request, **kwargs):
    categories = list(c.name for c in Category.objects.all())
    data = {'categories': categories}
    return JsonResponse(data)

def loadCategoryForLearner(request, **kwargs):
    categories = list(c.category.name for c in Course.objects.filter(status=0))
    categories.sort()
    data = {'categories': categories}
    return JsonResponse(data)
