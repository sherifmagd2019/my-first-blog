from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from . models import Post
from django.db.models.query import QuerySet
from users.models import Department
from django.shortcuts import render



def IN_ListView(request):
    template = 'home_in.html'
    context = {
    "queryset" : Post.objects.all().filter(departments__id = 4) 
    }
    return render (request, template, context)


 
#class IN_ListView(ListView):
#    model = Post
     
#    querySet=Post.objects.filter( departments__id=4 ) 
 #   #querySet = Department.objects.select_related('Post').filter(pk=6)
 #   context_object_name = querySet
#    template_name = 'home_in.html'
 




class BlogListView(ListView):
    model = Post
   # paginate_by = 3
    template_name = 'home.html'
    
    
    
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'  

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body','departments','otherpost']
    template_name = 'post_edit.html'    

class Blog_out_CreateView(CreateView):
    model = Post
    template_name = 'post_new_out.html'
    fields = ['title', 'body']
    
class Blog_in_CreateView(CreateView):
    model = Post
    template_name = 'post_new_out.html'
    fields = ['title', 'body']    
    

    
class BlogDetailView_Inposts(DetailView):
    model = Post
    template_name = 'post_detail.html' 
  #  queryset = Post.objects.filter(in_number__name='ACME Publishing')
  
  
def search_form(request):
    return render_to_response('search_form.html')  


def search_form_in(request):
    return render_to_response('search_form_in.html')  

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        posts = Post.objects.filter(title=q)
        return render_to_response('search_results.html',
                                  {'posts': posts, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
    
def search1(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        posts = Post.objects.filter(title=q)
        return render_to_response('search_results.html',
                                   {'posts': posts, 'query': q})
    elif 'q1' in request.GET and request.GET['q1']:
        q1 = request.GET['q1']
        posts = Post.objects.filter(body__icontains=q1)
        return render_to_response('search_results1.html',
                                  {'posts': posts, 'query': q1})    
    else:
        return HttpResponse('Please submit a search term.')    
    
     
def search_in(request):
    if 'q1' in request.GET and request.GET['q1']:
        q1 = request.GET['q1']
        posts = Post.objects.filter(organization=q1)
        return render_to_response('search_results_in.html',
                                  {'posts': posts, 'query': q1})
    else:
        return HttpResponse('Please submit a search term.')