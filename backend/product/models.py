from django.db import models
from slugify import slugify

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/product')
    description = models.TextField(db_index=True)
    price = models.FloatField()
    count = models.IntegerField()
    slug = models.SlugField(null=False, db_index=True, blank=True, max_length=200, unique=True)
    is_active = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'