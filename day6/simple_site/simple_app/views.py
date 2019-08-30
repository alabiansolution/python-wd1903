from django.shortcuts import render

# Create your views here.

def index(request):
	home_dict = {'home_key': 'Welocome to our Website'}
	return render(request, 'simple_app/index.html', context=home_dict)


def about(request):
	abt_dict = {'abt_key': 'Lean about our CEO'}
	return render(request, 'simple_app/about.html', context=abt_dict)

def contact(request):
	con_dict = {'con_key': 'Contact Us'}
	return render(request, 'simple_app/contact.html', context=con_dict)

