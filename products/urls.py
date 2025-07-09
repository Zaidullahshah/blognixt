from django.urls import path
from . import views
app_name = "products"
urlpatterns = [
    path('', views.ProductList, name="products-list"),
    path('<slug:item>', views.ProductView, name="product-view"),
    path('category/<slug:cat>', views.ProductCategory, name="product-category"),
    # path('disclaimer/', views.disclaimer_view, name='disclaimer'), 
]
