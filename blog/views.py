from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.urls import resolve

# Create your views here.
def all_blogs(request):
    current_url = resolve(request.path_info).url_name
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html',{'blogs':blogs,'current_url':current_url})

def detail(request,blog_id):
    current_url = resolve(request.path_info).url_name
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog,'current_url':current_url})

