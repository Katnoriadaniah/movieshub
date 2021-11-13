from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse


class Category(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

class Post(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='media')
	link = models.CharField(max_length=255)
	category = models.CharField(max_length=255, default = 'Hollywood')
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('home')