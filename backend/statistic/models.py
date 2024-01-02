from django.db import models


class DailyRequestCount(models.Model):
    date = models.DateField(unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'Requests on {self.date}: {self.count}'