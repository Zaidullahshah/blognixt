from django.contrib import admin
from .models import Blogs
from django_summernote.admin import SummernoteModelAdmin

class BlogsAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = 'body'

admin.site.register(Blogs, BlogsAdmin)