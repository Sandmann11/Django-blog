from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from . import get_crypto


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):        
        return self.name

    def get_absolute_url(self):
        return reverse('post_list')


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=225)
    lead = models.TextField(max_length=500, null=True)
    text = models.TextField()
    category = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='img', default='lus-200.jpg')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):        
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_list')