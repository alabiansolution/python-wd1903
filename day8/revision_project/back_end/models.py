from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Service(models.Model):
	service_title = models.CharField(max_length=100)
	service_desc = models.TextField(verbose_name='Service Description')

	def __str__(self):
		return self.service_title
		
class Category(models.Model):
	cat_name = models.CharField(verbose_name='Category Name', max_length=100)
	description = models.TextField(verbose_name='Description', blank=True, null=True)

	def __str__(self):
		return self.cat_name

class Post(models.Model):
	post_title = models.CharField(verbose_name='Post Title', max_length=150)
	category = models.ManyToManyField(Category, verbose_name='Categories of Post')
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
	post_img = models.ImageField(blank=True, null=True, upload_to='uploads/post_img', verbose_name='Post Image')
	create_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)
	content = models.TextField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.post_title

