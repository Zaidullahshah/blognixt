from django.http import JsonResponse, HttpResponse
from blogs.models import Blogs
from django.shortcuts import render
from products.models import Products,productCategory
from django.forms.models import model_to_dict
def getTagsData(request, tags, cur_id):
    tags_data = []
    for tag in tags.split(','):
        item = Products.objects.filter(tags__contains=tag).values('id', 'title', 'image','image_link', 'category', 'price', 'slug', 'stars').order_by('-id')[:10]
        for i in item[::-1]:
            iid = i['id']
            if iid == cur_id:
                continue
            isExist = 0
            for tg in tags_data:
                if tg['id'] == iid:
                    isExist = 1
                else:
                    continue
            if isExist == 0:
                tags_data.append(i)
    return JsonResponse({'tags_data': tags_data})

def getSideItems(request):
    recentBlogs = Blogs.objects.values('title', 'createdAt', 'image','image_link', 'slug', 'author', 'isNew', 'views')[:10]
    recentProducts = Products.objects.values('title', 'price', 'image', 'image_link','slug', 'isNew','views')[:10]
    category_list = productCategory.objects.values('name', 'slug')[:20]
    res = {}
    if recentBlogs:
        data = []
        for b in recentBlogs[::-1]:
            data.append(b)
        res['blogs'] = data
    if recentProducts:
        data = []
        for b in recentProducts[::-1]:
            data.append(b)
        res['products'] = data
    if category_list:
        data = []
        for b in category_list[::-1]:
            data.append(b)
        res['category_list'] = data
    return JsonResponse(res)


def SearchTerm(request, query):
    products = Products.objects.filter(title__contains = query).values('title', 'isNew', 'price', 'slug', 'image', 'image_link')[:8]
    blogs = Blogs.objects.filter(title__contains = query).values('title', 'isNew', 'author', 'createdAt', 'image', 'image_link', 'slug')[:8]
    categories = productCategory.objects.filter(name__contains = query).values('name', 'items', 'image', 'image_link', 'slug')[:8]
    length = len(products) + len(blogs) + len(categories)
    return JsonResponse({'items_length': length, 'products': list(products), 'blogs': list(blogs), 'categories': list(categories)})


def Home(request):
    categories = productCategory.objects.values('name', 'image', 'image_link', 'items', 'slug').order_by('-id')[:10]
    recentItems = Products.objects.filter(isActive=True).only('title', 'image','image_link', 'category', 'price', 'slug', 'isNew').order_by('-id')[:10]
    blogs = Blogs.objects.filter(isActive=True).values('title', 'image', 'image_link', 'sub_text','author', 'createdAt', 'slug', 'isNew').order_by('-id')[:6]
    return render(request, 'products/home.html', context={'categoriesList': categories, "recentItems": recentItems, 'blogs': blogs})

def About(request):
    return render(request, 'products/about.html', context={})
