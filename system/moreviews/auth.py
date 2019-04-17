import sys
sys.path.append("..")
from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template import loader
from django.template.loader import render_to_string
from django.views import View
from django.core.exceptions import SuspiciousOperation
from django.core.mail import EmailMessage
from ..forms import *
from ..models import *
from static import tokens

def loadHome(request,**kwargs):
	user=request.user
	if Instructor.objects.filter(pk=user.pk).exists():
		# print("instructor!")
		return redirect('/system/view/{}/'.format(user.pk))
	elif Learner.objects.filter(pk=user.pk).exists():
		# print("learner!")
		return redirect('/system/view/{}/'.format(user.pk))
	else:
		# admin
		return redirect('/system/auth/inviteInstructor/')

def sendInstructorLink(request,**kwargs):
	current_site = get_current_site(request)
	mail_subject = 'Register your instructor account.'
	tempUser=Instructor()
	if request.method=='POST':
		form=inviteInstructorForm(request.POST)
		data=request.POST.copy()
		tempUser.tempMail=data.get('email')
		tempUser.tempName=data.get('name')
		token=tokens.account_activation_token.make_token(tempUser)
		newToken=Token()
		newToken.token=token
		newToken.email=tempUser.tempMail
		newToken.save()
		if (form.is_valid()):
			message = render_to_string('instructorLink.html', {
				'name': data.get('name'),
				'domain': current_site.domain,
				# 'uid':tempUser.pk,
				'token':token,
			})
			email = EmailMessage(
						mail_subject, message, to=[tempUser.tempMail]
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
	token=kwargs['token']
	tempUser=Instructor()
	tempUser.tempName=kwargs['uidb64']
	valid=tokens.account_activation_token.check_token(tempUser, token)
	if (not valid) or Token.objects.filter(token=kwargs['token']).count()==0:
		return HttpResponse("Invalid token!")
	tokenObject=Token.objects.filter(token=kwargs['token'])[0]
	template=loader.get_template("registerInstructor.html")
	form=registerInstructorForm()
	context={'form':form,
			 'token':token,
			 'tempName':tempUser.tempName,
			 'email':tokenObject.email}
	return HttpResponse(template.render(context,request))

def createInstructorAccount(request,**kwargs):
	if request.method=='POST':
		form=registerInstructorForm(request.POST)
		data=request.POST.copy()
		token=data.get('token')
		email=data.get('email')
		tempUser=Instructor()
		tempUser.tempName=data.get('tempName')
		valid=tokens.account_activation_token.check_token(tempUser, token)
		if (not valid) or Token.objects.filter(token=token).count()==0:
			return HttpResponse("Invalid token!")

		if form.is_valid():
			newInstructor=form.save(commit=False)
			newInstructor.email=email
			newInstructor.save()

			tokenObject=Token.objects.filter(token=token)
			tokenObject=tokenObject[0]
			tokenObject.delete()
		else:
			return HttpResponse("Invalid user information!")
	return redirect('/accounts/login/')

def requestAccountLearner(request,**kwargs):
	template=loader.get_template("requestAccountLearner.html")
	form=requestAccountLearnerForm()
	context={'form':form}
	return HttpResponse(template.render(context,request))

def sendLearnerLink(request,**kwargs):
	if request.method=='POST':
		form=requestAccountLearnerForm(request.POST)
		data=request.POST.copy()
		staffID=data.get('staffID')

		#do checking with BANK SYSTEM
		target_email,first_name,last_name=None,"",""
		"info=BANK_SYSTEM_CHECK(staffID)"
		"email=info['email'], first_name=info['first_name'],last_name=info[last_name']"
		if staffID=='12345678':
			target_email='liuchangon7@gmail.com'
			first_name='chang'
			last_name='liu'
		elif staffID=='123':
			target_email = 'imon247@connect.hku.hk'
			first_name = 'y'
			last_name = 'li'
		#send email
		newUser=Learner()
		newUser.tempName=first_name+last_name
		newUser.tempMail=target_email
		current_site = get_current_site(request)
		mail_subject = 'Register your learner account.'
		token=tokens.account_activation_token.make_token(newUser)
		newToken=Token()
		newToken.token=token
		newToken.email=target_email
		newToken.save()
		if target_email is not None:
			message = render_to_string('learnerLink.html', {
				'name': first_name+last_name,
				'domain': current_site.domain,
				'token':token,
				'first_name':first_name,
				'last_name':last_name
			})
			email = EmailMessage(
						mail_subject, message, to=[target_email]
			)
			email.send()
			success=True
		else:
			success=False

		#show result
		template=loader.get_template("invitationResultLearner.html")
		print_email=target_email
		if print_email is not None and len(print_email)>3:
			print_email=[print_email[i] if i<3 else '*' for i in range(len(print_email))]
			print_email="".join(print_email)
		context={
			'name':first_name+last_name,
			'email':print_email,
			'res':success
		}
		return HttpResponse(template.render(context,request))

def registerLearner(request,**kwargs):
	token=kwargs['token']
	tempUser=Learner()
	first_name=kwargs['first_name']
	last_name=kwargs['last_name']
	tempUser.tempName=first_name+last_name
	valid=tokens.account_activation_token.check_token(tempUser, token)
	if (not valid) or Token.objects.filter(token=token).count()==0:
		return HttpResponse("Invalid token!")
	tokenObject=Token.objects.filter(token=token)[0]
	template=loader.get_template("registerLearner.html")
	form=registerLearnerForm()
	context={'form':form,
			 'token':token,
			 'tempName':tempUser.tempName,
			 'email':tokenObject.email,
			 'first_name':first_name,
			 'last_name':last_name}
	return HttpResponse(template.render(context,request))

def createLearnerAccount(request,**kwargs):
	if request.method=='POST':
		form=registerLearnerForm(request.POST)
		data=request.POST.copy()
		token=data.get('token')
		email=data.get('email')
		first_name=data.get('first_name')
		last_name=data.get('last_name')
		tempUser=Learner()
		tempUser.tempName=data.get('tempName')
		valid=tokens.account_activation_token.check_token(tempUser, token)
		if (not valid) or Token.objects.filter(token=token).count()==0:
			return HttpResponse("Invalid token!")

		if form.is_valid():
			newLearner=form.save(commit=False)
			newLearner.email=email
			newLearner.first_name=first_name
			newLearner.last_name=last_name
			newLearner.save()

			tokenObject=Token.objects.filter(token=token)
			tokenObject=tokenObject[0]
			tokenObject.delete()
		else:
			return HttpResponse("Invalid user information!")
	return redirect('/accounts/login/')
