from django.urls import path
from excercise_app import views


app_name = 'excercise_app'

urlpatterns = [
	path('', views.index, name='index'),
	# path('about_page/', views.about, name='about'),
	
]
