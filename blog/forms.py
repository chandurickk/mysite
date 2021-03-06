from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = {
			'title',
			'body',
			'status'
		}

class UserLoginForm(forms.Form):
	username = forms.CharField(label="")
	password = forms.CharField(label="", widget=forms.PasswordInput)