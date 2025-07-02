from django.shortcuts import render, get_object_or_404
from .models import Blogs
from django.core.paginator import Paginator

def view(request, slug):
    blog = get_object_or_404(Blogs, slug=slug)
    blog.views=blog.views + 1
    blog.save()
    return render(request, 'blogs/blog-view.html', context={'blog': blog})

def blogs(request, *args, **kwargs):
    blogs = Blogs.objects.values('title', 'sub_text','body', 'createdAt', 'image','image_link', 'author', 'slug', 'views').order_by('-id')
    paginator = Paginator(blogs, 25)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    return render(request, 'blogs/blogs-list.html', context={'page_obj': page_obj})