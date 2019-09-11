from django.urls import path
from revision_app import views

app_name = 'revision_app'

urlpatterns = [
    path('', views.about, name='about'),
    path('user_page/', views.users, name='users'),
    path('service_page/', views.service, name='service'),
    path('about_detail_page/<int:abt_id>', views.about_detail, name='about_detail'),
]
