
from django.urls import path, include
from back_end import views

app_name = 'back_end'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('confirm_logout/', views.confirm_logout, name='confirm_logout'),
    path('register/', views.register, name='register'),
    path('view_profile_page/', views.view_profile, name='view_profile'),
    path('edit_form_page/', views.edit_form, name='edit_form'),
    path('pass_form_page/', views.pass_form, name='pass_form'),
    path('add_form_page/', views.AddPost.as_view(), name='add_form'),
    path('list_post_page/', views.ListPost.as_view(), name='list_post'),
    path('detail_post_page/<int:pk>', views.DetailPost.as_view(), name='detail_post'),
    path('accounts/', include('django.contrib.auth.urls')),
]