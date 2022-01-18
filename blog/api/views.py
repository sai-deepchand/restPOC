from blog.models import Blog
from blog.api.serializers import BlogSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

class BlogList(generics.ListCreateAPIView):
       queryset = Blog.objects.all()
       serializer_class = BlogSerializer
       authentication_classes = [TokenAuthentication]
       permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

       def perform_create(self, serializer):
              serializer.save(author=self.request.user)
       
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
       queryset = Blog.objects.all()
       serializer_class = BlogSerializer
       authentication_classes = [TokenAuthentication]
       permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]              
                   