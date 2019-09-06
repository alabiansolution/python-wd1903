from django.urls import path
from revision_app import views
from revision_app import form_views

app_name = 'revision_app'

urlpatterns = [
    path('', views.about, name='about'),
    path('user_page/', views.users, name='users'),
    path('service_page/', views.service, name='service'),
    path('form1/', form_views.django_form1, name='django_form1'),
    path('form2/', form_views.django_form2, name='django_form2'),
    path('widget/', form_views.form_widget, name='form_widget'),
    path('form_validators/', form_views.form_validators, name='form_validators'),
    path('about_detail_page/<int:abt_id>', views.about_detail, name='about_detail'),
]
