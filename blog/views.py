from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from blog.models import Blog
from django.views.generic import (
       ListView, DetailView, 
       CreateView, UpdateView,
       DeleteView
)

# def home(request):
#        return render(request, 'blog/home.html',{"blogs":Blog.objects.all()})

class BlogHome(ListView):
       model = Blog
       template_name = 'blog/home.html'
       context_object_name = 'blogs'
       ordering = ['-date_posted']
       
class BlogDetail(DetailView):
       model = Blog
       template_name = 'blog/detail.html'
       context_object_name = 'blog'

class BlogCreate(LoginRequiredMixin,CreateView):
       model = Blog
       fields = ['heading','msg']
       template_name = 'blog/create.html'

       def form_valid(self, form) :
              form.instance.author = self.request.user
              return super().form_valid(form)

class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
       model = Blog
       fields = ['heading','msg']
       template_name = 'blog/create.html'

       def form_valid(self, form) :
              form.instance.author = self.request.user
              return super().form_valid(form)
       
       def test_func(self) :
              blog = self.get_object()
              return self.request.user == blog.author
              
class BlogDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
       model = Blog
       template_name = 'blog/delete.html'
       context_object_name = 'blog'

       success_url = '/blog'

       def test_func(self) :
              blog = self.get_object()
              return self.request.user == blog.author