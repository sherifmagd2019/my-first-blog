# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('signup/', views.SignUp.as_view(), name='signup'),
     path('dep/new/', views.DepCreateView.as_view(success_url="users/success/"), name='dep_new'),
      
]