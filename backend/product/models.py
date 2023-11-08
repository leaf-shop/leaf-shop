from django.contrib.auth import get_user_model
from discount.models import Discount
from share_module.models import Category
from django.db import models
from slugify import slugify


class Attribute(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False, blank=True)


class ProductGallery(models.Model):
    alt = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/product')


class Product(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(
        upload_to='images/product', null=True, blank=True)
    Category = models.ManyToManyField(Category, related_name="productCategory", null=True, blank=True)
    gallery = models.ManyToManyField(
        ProductGallery, null=True, blank=True, related_name="productGallery")
    description = models.TextField(db_index=True)
    price = models.FloatField()
    discount = models.ForeignKey(
        Discount, on_delete=models.CASCADE, null=True, blank=True, related_name="products")
    attribute = models.ManyToManyField(
        Attribute, null=True, blank=True, related_name="products")
    count = models.IntegerField()
    slug = models.SlugField(null=False, db_index=True,
                            blank=True, max_length=200, unique=True)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Comment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments")
    SCORES = (
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Great')
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    score = models.CharField(max_length=1, choices=SCORES)
    created_datetime = models.DateTimeField(auto_now_add=True)
    demonstrable = models.BooleanField(default=True)
    recommendable = models.BooleanField(default=True)
