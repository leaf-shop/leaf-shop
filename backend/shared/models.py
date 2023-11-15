from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    parent = models.ForeignKey('Category', models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    product = models.ForeignKey("product.Product", null=True, blank=True,
        on_delete=models.CASCADE, related_name="comments")
    blog = models.ForeignKey("blog.Blog", null=True, blank=True,
        on_delete=models.CASCADE, related_name="comments")
    SCORES = (
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Great')
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    descriptions = models.TextField()
    score = models.CharField(max_length=1, choices=SCORES)
    created_datetime = models.DateTimeField(auto_now_add=True)
    demonstrable = models.BooleanField(default=True)
    recommendable = models.BooleanField(default=True)

    def __str__(self):
        return self.descriptions
