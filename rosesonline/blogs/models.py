from django.db import models
from django.template.defaultfilters import slugify
import os
from django.dispatch import receiver
from django_resized import ResizedImageField


class IpModel(models.Model):
    ip = models.CharField(max_length=100);
    def __str__(self):
        return self.ip

class Blogs(models.Model):
    title = models.CharField(max_length=512, blank=False,
                             help_text='Enter title here')
    body = models.TextField(blank=False, help_text='Enter full text here', verbose_name='Full Description')
    sub_text = models.TextField(
        blank=True,
         verbose_name='short description')
    image = ResizedImageField(size=[640, 426], upload_to="blogs/", blank=True, default="")
    image_link = models.CharField(max_length=2048, blank=True, help_text="Enter image url here...")
    slug = models.SlugField(unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255, blank=False)
    tags = models.CharField(max_length=500, blank=True, default='')
    keywords = models.CharField(max_length=500, blank=True, default='')
    views = models.IntegerField(default=539, blank=True, verbose_name="Post Views")
    isNew = models.BooleanField(default=True, blank=False, help_text='this item is new?', verbose_name='is new')
    isActive = models.BooleanField(default=True, blank=False, help_text='enable and disable the product on view.', verbose_name='is active')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return  super().save(*args, **kwargs)


@receiver(models.signals.post_delete, sender=Blogs)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Blogs)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Blogs.objects.get(pk=instance.pk).image
    except Blogs.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
