from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from django import forms
from .models import Blogs


class BlogsAdminForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'


@admin.register(Blogs)
class BlogsAdmin(SummernoteModelAdmin):
    form = BlogsAdminForm
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

    list_display = ('title', 'author', 'createdAt', 'isActive', 'image_preview')
    list_filter = ('author', 'isActive', 'createdAt')
    search_fields = ('title', 'body')
    ordering = ('-createdAt',)

    readonly_fields = ('image_preview', 'createdAt')

    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" width="150" style="border-radius:4px;" />', obj.image.url)
        return "No Image Uploaded"
    image_preview.short_description = "Current Image"

    def get_fieldsets(self, request, obj=None):
        base_fields = (
            (None, {
                'fields': ('title', 'slug', 'author', 'isActive')
            }),
            ('Image', {
                'fields': ('image', 'image_preview')
            }),
            ('Content', {
                'fields': ('body',)
            }),
        )
        if obj:
            base_fields += (('Meta Info', {'fields': ('createdAt',)}),)
        return base_fields
