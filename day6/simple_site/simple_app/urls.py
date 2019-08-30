from django.urls import path
from simple_app import views

app_name = 'simple_app'

urlpatterns = [
	path('', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
]
