from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, post_delete, post_delete, pre_save
from django.dispatch import receiver
from django_resized import ResizedImageField
import os


class productCategory(models.Model):
    name = models.CharField(max_length=255, blank=False, default='default')
    items = models.IntegerField(default=0, blank=True)
    image = ResizedImageField(
        size=[640, 426], blank=True, upload_to='categories/')
    image_link = models.CharField(max_length=2048, blank=True, help_text="Enter image url here...")
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


def default_category():
    return productCategory.objects.get(slug="default").pk


class Products(models.Model):
    category = models.ForeignKey(
        productCategory, on_delete=models.SET_DEFAULT, default=default_category)
    title = models.CharField(
        max_length=512, help_text='Enter product title here')
    image = ResizedImageField(
        size=[640, 426], blank=True, upload_to="products/")
    image_link = models.CharField(max_length=2048, help_text='Enter image url here', blank=True, default="")
    link = models.CharField(
        max_length=2048, help_text='Enter product url here')
    short_desc = models.TextField(
                                  help_text='Add a short description of product.', default='', blank=True)
    description = models.TextField(
        help_text='Add something about this item', default='', blank=True)
    ratings = models.IntegerField(blank=True, default=31)
    stars = models.DecimalField(blank=True, default=1, max_digits=2, decimal_places=1)
    slug = models.SlugField(null=False, unique=True)
    price = models.DecimalField(
        decimal_places=2, max_digits=10, blank=True, default=0.00)
    tags = models.CharField(max_length=500, blank=True, default='')
    keywords = models.CharField(max_length=500, blank=True, default='')
    views = models.IntegerField(default=689, blank=True, verbose_name="Post Views")
    isNew = models.BooleanField(default=True, blank=False, help_text='this item is new?', verbose_name='is new')
    isActive = models.BooleanField(default=True, blank=False, help_text='enable and disable the product on view.', verbose_name='is active')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


@receiver(post_save, sender=Products)
def _post_save_receiver(sender, instance=None, **kwargs):
    id = instance.category.pk
    cat = productCategory.objects.get(pk=id)
    cat.items = cat.items + 1
    cat.save()


@receiver(post_delete, sender=Products)
def _post_delete_receiver(sender, instance=None, **kwargs):
    id = instance.category.pk
    cat = productCategory.objects.get(pk=id)
    cat.items = cat.items - 1
    cat.save()


@receiver(models.signals.post_delete, sender=productCategory)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image and instance.image != '':
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=productCategory)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = productCategory.objects.get(pk=instance.pk).image
        if old_file == '':
            return False
    except productCategory.DoesNotExist:
        return False
    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
