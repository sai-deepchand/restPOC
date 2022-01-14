from django.urls import path
from . import views


urlpatterns = [
#     path('', views.home,name='blog-home'),
       path('', views.BlogHome.as_view(),name='blog-home'),
       path('<int:pk>/', views.BlogDetail.as_view(),name='blog-detail'),
       path('create/', views.BlogCreate.as_view(),name='blog-create'),
       path('<int:pk>/update', views.BlogUpdate.as_view(),name='blog-update'),
       path('<int:pk>/delete', views.BlogDelete.as_view(),name='blog-delete'),
]      
