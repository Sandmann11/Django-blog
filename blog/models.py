from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from . import get_crypto


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=225)
    lead = models.TextField(max_length=500, null=True)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='img', default='lus-200.jpg')
    created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):        
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('post_text', kwargs={'pk': self.pk})
        return reverse('post_list')






    
    
# class Crypto(models.Model):
#     name = models.CharField(max_length=50)
#     symbol = models.CharField(max_length=5)
#     # price = models.FloatField(max_length=15)
#     date = models.DateTimeField(default=timezone.now)

#     def date_added(self):
#         self.date = timezone.now()
#         self.save()

#     def __str__(self):        
#         return self.symbol + ' |  ' + str(self.name)
