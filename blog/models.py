from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
       heading = models.CharField(max_length=50)
       msg = models.TextField(max_length=500)
       date_posted = models.DateTimeField(auto_now_add=True)
       date_updated = models.DateTimeField(auto_now=True)
       author = models.ForeignKey(User, on_delete=models.CASCADE)        

       def __str__(self):
              return  f" {self.heading}  - by {self.author} "

       def get_absolute_url(self):
              return reverse('blog-detail',kwargs={'pk':self.pk})
       
              