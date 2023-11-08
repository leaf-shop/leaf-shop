from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    parent = models.ForeignKey('Category', models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
