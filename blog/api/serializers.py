from urllib import request
from rest_framework import serializers

from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
       author = serializers.SerializerMethodField('get_author')
       class Meta:
              model = Blog
              fields = ['id','heading', 'msg', 'date_posted','date_updated','author']
         
       def get_author(self,blogpost):
              author = blogpost.author.username
              return author