import sys
sys.path.append("..")
from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template import loader
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views import View
from django.core.exceptions import SuspiciousOperation
from django.core.mail import EmailMessage
from ..forms import *
from ..models import *
from static import tokens

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

def sendInstructorLink(request,**kwargs):
	current_site = get_current_site(request)
	mail_subject = 'Register your instructor account.'
	tempUser=User.objects.get(username='abc')
	print(tempUser)
	# tempUser.pk=123
	message = render_to_string('instructorRegistration.html', {
		'user': tempUser,
		'domain': current_site.domain,
		'uid':tempUser.pk,
		'token':tokens.account_activation_token.make_token(tempUser),
	})
	to_email = 'liuchangon7@gmail.com'
	email = EmailMessage(
				mail_subject, message, to=[to_email]
	)
	email.send()

def registerInstructor(request,**kwargs):
	pass