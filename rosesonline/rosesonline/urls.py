from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from . import views
app_name = 'rosesonline'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('about/', views.About, name='about'),
    path('products/', include('products.urls')),
    path('blogs/', include('blogs.urls')),
    path('api/get-side-view/', views.getSideItems, name='side-bar-api'),
    path('api/get-tags-data/<str:tags>/<int:cur_id>/', views.getTagsData, name='tag-data'),
    path('api/search/<str:query>', views.SearchTerm, name='tag-data'),
    path('summernote/', include('django_summernote.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)