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
		return redirect('/system/view/{}/'.format(user.pk))
	elif isinstance(user,Learner):
		print("learner!")
		return redirect('/system/view/{}/'.format(user.pk))
	return redirect('/system/auth/inviteInstructor/'.format(user.pk))

def sendInstructorLink(request,**kwargs):
	current_site = get_current_site(request)
	mail_subject = 'Register your instructor account.'
	tempUser=request.user
	if request.method=='POST':
		form=inviteInstructorForm(request.POST)
		data=request.POST.copy()
		tempUser.instructorName=data.get('name')
		if (form.is_valid()):
			message = render_to_string('instructorRegistration.html', {
				'name': data.get('name'),
				'domain': current_site.domain,
				'uid':tempUser.pk,
				'token':tokens.account_activation_token.make_token(tempUser),
			})
			to_email = data.get('email')
			email = EmailMessage(
						mail_subject, message, to=[to_email]
			)
			email.send()
			success=True
		else:
			success=False
		template=loader.get_template("invitationResult.html")
		context={
			'name':data.get('name'),
			'email':data.get('email'),
			'res':success
		}
		return HttpResponse(template.render(context,request))

def inviteInstructor(request,**kwargs):
	user=request.user
	if user.is_superuser:
		template=loader.get_template("inviteInstructor.html")
		form=inviteInstructorForm()
		context={'form':form}
		return HttpResponse(template.render(context,request))
	else:
		raise SuspiciousOperation("Only admin can invite Instructor!")


def registerInstructor(request,**kwargs):
	print("hello")
	template=loader.get_template("registerInstructor.html")
	form=registerInstructorForm()
	context={'form':form}
	return HttpResponse(template.render(context,request))

def createInstructorAccount(request,**kwargs):
	if request.method=='POST':
		form=registerInstructorForm(request.POST)
		newInstructor=form.save(commit=False)
		newInstructor.save()

	