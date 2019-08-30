from django.urls import path
from revision_app import views


app_name = 'revision_app'

urlpatterns = [
	path('', views.about, name='about'),
	path('service_page/', views.service, name='service'),
]
