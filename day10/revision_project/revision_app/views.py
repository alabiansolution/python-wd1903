from django.shortcuts import render
from revision_app.models import About, Service
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	show_service = Service.objects.all()

	show_about = About.objects.all()

	home_dict = {
		'serv_key':show_service,
		'abt_key':show_about
	}

	return render(request, 'front_end/index.html', context=home_dict)

def about(request):
	list_abt = About.objects.all()
	return render(request, 'front_end/about.html', {'abt_list':list_abt})

def users(request):
	list_usr = User.objects.all()
	return render(request, 'front_end/users.html', {'usr_list':list_usr})

def service(request):
	list_srv = Service.objects.all()
	return render(request, 'front_end/services.html', {'srv_list':list_srv})

def about_detail(request, abt_id):
	about_detail = About.objects.get(pk=abt_id)
	return render(request, 'front_end/detail.html', {'abt_det':about_detail})
