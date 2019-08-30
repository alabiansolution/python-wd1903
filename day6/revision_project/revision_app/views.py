from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	return render(request, 'revision_app/index.html', {'home_key':'Welcome to my hood'})
	


def about(request):
	abt_dict = {
		'abt_key': 'About Us',
		'content' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam sit ipsa a quidem eveniet ipsum odio ex ratione voluptatem expedita eligendi maiores perspiciatis, sint natus officiis doloremque modi ducimus, omnis.'
	}
	return render(request, 'revision_app/about.html', context=abt_dict)
	

def service(request):
	ser_dict = {
		'serv0': 'Our Services',
		'serv1':'Web Development',
		'serv2':'Desktop App',
		'serv3':'Mobile App',
	 }
	return render(request, 'revision_app/service.html', ser_dict)

