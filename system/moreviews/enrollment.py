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

def enrollInCourse(request, **kwargs):
    template = loader.get_template("enrollmentResult.html")
    learner = Learner.objects.filter(id=request.user.id)[0]
    course = Course.objects.filter(id=kwargs['course_id'])[0]
    is_enrolled = Enroll.objects.filter(course__id=kwargs['course_id'], learner__id=request.user.id)
    if len(is_enrolled)>0:
        disabled = 'true'
    else:
        new_enroll = Enroll(
            learner = learner,
            course = course,
            progress = 0,
            status = False
        )
        new_enroll.save()
        disabled = 'false'
    context = {
        'course': course,
        'learner': learner,
        'disabled': disabled
    }
    return HttpResponse(template.render(context, request))
