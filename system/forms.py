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
		if email_again!=email:
			raise ValidationError("Email mismatch!",code='invalid')

class registerInstructorForm(ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model=Instructor
		fields = ['username','first_name','last_name','autobiagraphy']

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class requestAccountLearnerForm(forms.Form):
	staffID=forms.CharField(label='staff ID',max_length=8)

class registerLearnerForm(ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model=Learner
		fields = ['username']

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

