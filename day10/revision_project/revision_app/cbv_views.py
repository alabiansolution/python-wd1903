from django.shortcuts import render
from revision_app.models import Post
from revision_app.forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PostList(ListView):
	model = Post
	template_name = 'front_end/post_list.html'
	context_object_name = 'post_list'


class PostDetail(DetailView):
	model = Post
	template_name = 'front_end/detail_post.html'
	context_object_name = 'detail_post'

class CreatePost(CreateView):
	model = Post
	template_name = 'front_end/cbv_post_form.html'
	form_class = PostForm
	success_url = reverse_lazy('revision_app:post_list')


class UpdatePost(UpdateView):
	model = Post
	template_name = 'front_end/cbv_post_form.html'
	form_class = PostForm
	success_url = reverse_lazy('revision_app:post_list')

class DeletePost(DeleteView):
	model = Post
	template_name = 'front_end/confirm_delete.html'
	success_url = reverse_lazy('revision_app:post_list')




