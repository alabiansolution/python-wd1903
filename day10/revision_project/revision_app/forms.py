from django import forms
from django.core import validators
from revision_app.models import ContactModel1, Category, Post
from django.contrib.auth.models import User
from tinymce import TinyMCE

class DjangoForm1(forms.Form):
	name = forms.CharField()
	subject = forms.CharField(required=False, max_length=7)
	email = forms.EmailField()
	very_email = forms.EmailField()
	message = forms.CharField(required=False, widget=forms.Textarea)


class FormWiget(forms.Form):
	GENDER_CHOICE = [
	('male', 'Male'),
	('female', 'Female')
	]

	REFERER_CHOICE = [
	('facebook', 'Facebook'),
	('twitter', 'Twitter'),
	('nairaland', 'Nairaland'),
	]
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	subject = forms.CharField(required=False, max_length=7, 
		widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Subject'}))
	gender = forms.CharField(required=False, widget=forms.RadioSelect(choices=GENDER_CHOICE))
	referer = forms.CharField(required=False, 
					widget=forms.Select(attrs={'class':'form-control'}, choices=REFERER_CHOICE))
	email = forms.EmailField(disabled=True)
	message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    
    


def check_for_c(value):
	if value[0].lower() != 'c':
		raise forms.ValidationError('name must start with c')

class FormValidation(forms.Form):
	name = forms.CharField(validators=[check_for_c])
	subject = forms.CharField(required=False)
	email = forms.EmailField()
	very_email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)
	botcather = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

	def clean_email(self):
		email = self.cleaned_data['email']

		if not email.endswith('@alabiansolutions.com'):
			raise forms.ValidationError('Email must end with @alabiansolutions.com')


	def clean(self):
		cleaned_data = super().clean()

		email1 = cleaned_data['email']
		email2 = cleaned_data['very_email']

		if email1 != email2:
			raise forms.ValidationError('Email and Verify Email are not the same')

class ContactForm1(forms.ModelForm):

	class Meta():
		model = ContactModel1
		fields = ('name', 'email', 'referer', 'content')
		widgets = {
			'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter name'}),
			'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter email'}),
			'referer':forms.Select(attrs={'class':'form-control'}),
			'content':forms.Textarea(attrs={'class':'form-control'}),

		}
		# fields = '__all__'
		# exclude = ('content', 'referer')

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):

	category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
	author = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='Choose Author')

	content = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 10}))

	class Meta():
		model = Post
		fields = ('post_title', 'category', 'author', 'post_img')