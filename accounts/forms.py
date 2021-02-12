from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "input100",
				"placeholder":"Enter Username"
			}))
	email = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "input100",
				"placeholder": "Enter Email"
			}))
	password1 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class": "input100",
				"placeholder": "Enter Password"
			}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class": "input100",
				"placeholder": "Confirm Password"
			}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1','password2']

