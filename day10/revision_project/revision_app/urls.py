from django.urls import path
from revision_app import views
from revision_app import form_views
from revision_app import cbv_views

app_name = 'revision_app'

urlpatterns = [
    path('', views.about, name='about'),
    path('user_page/', views.users, name='users'),
    path('service_page/', views.service, name='service'),
    path('form1/', form_views.django_form1, name='django_form1'),
    path('form2/', form_views.django_form2, name='django_form2'),
    path('widget/', form_views.form_widget, name='form_widget'),
    path('form_validators/', form_views.form_validators, name='form_validators'),
    path('thanku/', form_views.thanks, name='thanks'),
    path('contact_form1_page/', form_views.contact_form1, name='contact_form1'),
    path('post_form_page/', form_views.post_form, name='post_form'),
    path('about_detail_page/<int:abt_id>', views.about_detail, name='about_detail'),
    path('post_list/', cbv_views.PostList.as_view(), name='post_list'),
    path('post_detail_page/<int:pk>', cbv_views.PostDetail.as_view(), name='post_detail'),
    path('create_post_page/', cbv_views.CreatePost.as_view(), name='create_post'),
    path('update_post_page/<int:pk>', cbv_views.UpdatePost.as_view(), name='update_post'),
    path('delete_post_page/<int:pk>', cbv_views.DeletePost.as_view(), name='delete_post'),
]
