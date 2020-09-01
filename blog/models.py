from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	product = models.CharField(max_length=100)
	content = models.TextField()
	date_product = models.DateTimeField(default=timezone.now) #auto_now_add=True
	owner = models.ForeignKey(User,on_delete=models.CASCADE) #if the user is deleted also the post will be deleted. User is a table.

	def __str__(self):
		return self.product


	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})