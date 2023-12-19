from django.conf import settings
from django.db import models
from product import models as product_models
from datetime import datetime


class Order(models.Model):
    STATUS_OPTIONS = (
        ('c', 'Cancelled'),
        ('p', 'Paid'),
        ('u', 'Unpaid')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_OPTIONS,
        default=STATUS_OPTIONS[2][0])

    def calculate_price(self):
        return sum([item.total_price() for item in self.items.all()])

    def calculate_price_with_discount(self):
        price = 0
        for item in self.items.all():

            discount = item.product.discount
            total_price = item.total_price()

            if not discount:
                price += total_price
                continue

            condition = discount.start_date > datetime.now() > discount.expire_date

            if condition: continue

            if discount.type == discount.DISCOUNT_TYPES_NUMBER:
                price += total_price - discount.value
            else:
                price += total_price - (total_price * discount.value / 100)

        return price

    def change_status_to_paid_order(self):
        self.status = self.STATUS_OPTIONS[1][0]
        self.save()

    def change_status_to_cancelled_order(self):
        self.status = self.STATUS_OPTIONS[0][0]
        self.save()

    def change_status_to_unpaid_order(self):
        self.status = self.STATUS_OPTIONS[2][0]
        self.save()

    def __str__(self) -> str:
        return f"{self.user.username} -- {self.datetime_created}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, blank=True, null=True, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(
        product_models.Product, blank=True, null=True, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=1)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"{self.order} -- {self.product}"
