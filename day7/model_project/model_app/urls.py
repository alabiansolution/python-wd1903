from django.urls import path
from model_app import views

app_name = 'model_app'


urlpatterns = [
	path('', views.about, name='about'),
	path('users_page/', views.users, name='users'),
	
]