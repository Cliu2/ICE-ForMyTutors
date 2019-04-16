from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from system.models import *



class enterModuleInfo(forms.Form):
	post = forms.CharField()

class inviteInstructorForm(forms.Form):
	name=forms.CharField(label='Instructor name', max_length=100)
	email=forms.EmailField(max_length=200,label='Email')
	email_again=forms.EmailField(max_length=200,label='Confirm Email')

	def clean(self):
		cleaned_data = super().clean()
		email=cleaned_data.get("email")
		email_again=cleaned_data.get("email_again")
		print(email_again,email)
		if email_again!=email:
			raise ValidationError("Email mismatch!",code='invalid')

class registerInstructorForm(ModelForm):
	# username=forms.CharField(label='account',max_length=200)
	# password_again=forms.CharField(label='password',widget=forms.PasswordInput)
	# password_again=forms.CharField(label='retype password',widget=forms.PasswordInput)
	# firstname=forms.CharField(label='first name', max_length=100)
	# lastname=forms.CharField(label='last name', max_length=100)
	# autobiagraphy=forms.CharField(label='autobiagraphy',widget=forms.Textarea)


	class Meta:
		model=Instructor
		fields = ['username','password',
			'first_name','last_name','autobiagraphy']
