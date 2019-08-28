from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def base(request):
	return HttpResponse('I love Python')

def base1(request):
	return HttpResponse('<h2>We are here!</h2>')

def index(request):
	home_dic = {
				'home_key':'Welcome to my home page',
				'content_key':'Here are my content which is here'
				}
	return render(request, 'excercise_app/index.html', context=home_dic)