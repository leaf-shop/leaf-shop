from django.db import models


class Discount(models.Model):
    DISCOUNT_TYPES_NUMBER = "n"
    DISCOUNT_TYPES_PERCENT = "p"
    DISCOUNT_TYPES = (
        (DISCOUNT_TYPES_NUMBER, "Number"),
        (DISCOUNT_TYPES_PERCENT, "Percent")
    )
    title = models.CharField(max_length=100)
    value = models.PositiveIntegerField()
    type = models.CharField(max_length=1, choices=DISCOUNT_TYPES)
    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()
