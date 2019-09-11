from django.shortcuts import render, redirect
from back_end.forms import RegForm, EditUserForm, PostForm
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash 
from django.contrib import messages
from back_end.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(
	ListView, DetailView, UpdateView, DeleteView, CreateView)
from django.urls import reverse_lazy
# Create your views here.

@login_required
def dashboard(request):
	return render(request, 'back_end/index.html')

@login_required
def confirm_logout(request):
	return render(request, 'registration/confirm_logout.html')


def register(request):
	if request.method == 'POST':
		register_form = RegForm(request.POST)
		if register_form.is_valid():
			register_form.save()
			return redirect('back_end:login')
	else:
		register_form = RegForm()
	return render(request, 'registration/register.html', {'reg':register_form})

@login_required
def pass_form(request):
	if request.method == 'POST':
		pass_form = PasswordChangeForm(data=request.POST, user=request.user)
		if pass_form.is_valid():
			pass_form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, 'Password changed successfully.')
			
	else:
		pass_form = PasswordChangeForm(user=request.user)
	return render(request, 'back_end/pass_form.html', {'pass_key':pass_form})

@login_required
def edit_form(request):
	if request.method == 'POST':
		edit_form = EditUserForm(request.POST, instance=request.user)
		if edit_form.is_valid():
			edit_form.save()
			messages.success(request, 'User edited successfully.')
			
	else:
		edit_form = EditUserForm(instance=request.user)
	return render(request, 'back_end/edit_form.html', {'edit_key':edit_form})

@login_required
def view_profile(request):
	return render(request, 'back_end/view_profile.html', {'profile':request.user})


class AddPost(LoginRequiredMixin, CreateView):
	template_name = 'back_end/post.html'
	form_class = PostForm
	model = Post
	success_url = reverse_lazy('back_end:dashboard')

class ListPost(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'back_end/list_post.html'
	context_object_name = 'list_post'

class DetailPost(LoginRequiredMixin, DetailView):
	model = Post
	template_name = 'back_end/detail_post.html'
	context_object_name = 'detail_post'