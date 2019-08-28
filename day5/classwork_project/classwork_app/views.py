from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def base(request):
	return HttpResponse('<h1>Hello World!</h1>')

def base2(request):
	return HttpResponse('<h1>Another Base</h1>')
