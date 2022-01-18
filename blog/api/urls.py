from django.urls import path
from blog.api import views

urlpatterns = [
    path('', views.BlogList.as_view()),
    path('<int:pk>', views.BlogDetail.as_view()),
]
     