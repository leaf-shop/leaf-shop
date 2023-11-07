from django.db import models


class Discount(models.Model):
    DISCOUNT_TYPES = (
        ("n", "Number"),
        ("p", "Percent")
    )
    title = models.CharField(max_length=100)
    value = models.PositiveIntegerField()
    type = models.CharField(max_length=1, choices=DISCOUNT_TYPES)
    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()
