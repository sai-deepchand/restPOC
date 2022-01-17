
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from users.views import register_request,login_request,logout_request


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('api/',include('blog.api.urls')),
    path('register/',register_request,name='register'),
     path("login/", login_request, name="login"),
     path("logout/", logout_request, name= "logout"),
]
