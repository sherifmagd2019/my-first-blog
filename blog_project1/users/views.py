# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render_to_response
from django.http import HttpResponse
from users.models import  Department
from django.urls import reverse





from .forms import CustomUserCreationForm



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    

class DepCreateView(CreateView):
    model = Department
    template_name = 'dep_new.html'
    fields = '__all__'  
    
    def get_success_url(self):
            return reverse('dep_new')
    

class DepUpdateView(UpdateView):
    model = Department
    fields = '__all__'  
    template_name = 'dep_edit.html'     
    
class BlogDetailView(DetailView):
    model = Department
    template_name = 'dep_detail.html'
        
    