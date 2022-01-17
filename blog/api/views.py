import imp
from re import template
from blog.models import Blog
# from django.contrib.auth.models import User
from blog.api.serializers import BlogSerializer
from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.authtoken.models import Token

# token = Token.objects.create(user=)
# print(token.key)

class BlogList(generics.ListCreateAPIView):
       queryset = Blog.objects.all()
       serializer_class = BlogSerializer
       # context_object_name = 'blogs'
       template_name = 'api.html'


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer