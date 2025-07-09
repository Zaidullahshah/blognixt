from django.shortcuts import render, get_object_or_404
from .models import Products,productCategory
from django.core.paginator import Paginator

def ProductView(request, item):
    Products.objects.get(slug=item)
    product = get_object_or_404(Products,slug=item)
    product.views=product.views + 1
    product.save()
    categoriesList = productCategory.objects.all()
    return render(request, 'products/product-view.html', context={'product':product, 'categoriesList': categoriesList})

def ProductCategory(request, cat):
    category_name = get_object_or_404(productCategory,slug=cat)
    categoriesList = productCategory.objects.all()
    products = Products.objects.filter(category=category_name.id).values('title', 'image','image_link', 'category', 'link', 'price', 'slug').order_by('-id')
    paginator = Paginator(products, 35)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/product-category.html', context={'page_obj':page_obj, 'categoriesList': categoriesList, 'category_name': category_name})
    
    

def ProductList(request):
    categoriesList = productCategory.objects.all()
    products = Products.objects.filter(isActive=True).only('title', 'image','image_link', 'category', 'price', 'slug', 'isNew').order_by('-id')
    paginator = Paginator(products, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/product-list.html', context={'page_obj': page_obj, 'categoriesList': categoriesList})

# def disclaimer_view(request):
#     return render(request, 'disclaimer.html')

