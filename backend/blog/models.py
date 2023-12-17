from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify
from shared.models import Category



class Blog(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/blog', blank=True, null=True)
    description = models.TextField()
    category = models.ManyToManyField(Category, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(null=False, db_index=True,
                            blank=True, max_length=200, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
