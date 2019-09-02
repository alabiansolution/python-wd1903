from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	website = models.URLField(null=True, blank=True)
	age = models.IntegerField(null=True, blank=True)
	your_cv = models.FileField(null=True, blank=True, upload_to='uploads/pdf')
	def __str__(self):
		return self.user.username

class Category(models.Model):
	cat_name = models.CharField(verbose_name='Category Name', max_length=100)
	cat_description = models.TextField(verbose_name='Category Description', null=True, blank=True)

	def __str__(self):
		return self.cat_name

class Post(models.Model):
	post_title = models.CharField(max_length=100)
	post_content = models.TextField()
	post_image = models.FileField(blank=True, null=True, upload_to='uploads/post_img')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ManyToManyField(Category)
	create_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.post_title




