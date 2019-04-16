from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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

