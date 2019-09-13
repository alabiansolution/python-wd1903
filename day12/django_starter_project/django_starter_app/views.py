from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'django_starter_app/index.html', {'home_key':'Welcome here'})
