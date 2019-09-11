from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm 
from back_end.models import Post, Category


class RegForm(UserCreationForm):

	class Meta():
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')



class EditUserForm(UserChangeForm):

	class Meta():
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

class PostForm(forms.ModelForm):
	category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
	author = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='Choose Author')

	class Meta():
		model = Post
		fields = ('post_title', 'author', 'category', 'post_img', 'content')

