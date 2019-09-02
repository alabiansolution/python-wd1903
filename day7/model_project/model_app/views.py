from django.shortcuts import render
from django.contrib.auth.models import User
from model_app.models import Post


# Create your views here.


def index(request):
	list_post = Post.objects.all()
	return render(request, 'model_app/index.html', {'post_key':list_post})

def about(request):
	return render(request, 'model_app/about.html', {'about_key':'About Us'})
	
def users(request):
	list_users = User.objects.all()
	return render(request, 'model_app/users.html', {'list_key':list_users})
