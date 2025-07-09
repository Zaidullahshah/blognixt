from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Products, productCategory

class productCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ProductsAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = 'description'

admin.site.register(Products, ProductsAdmin)
admin.site.register(productCategory, productCategoryAdmin)