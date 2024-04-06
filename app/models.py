from django.db import models


class House(models.Model):
    title = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    location_date = models.CharField(max_length=256)

    def __str__(self):
        return self.title
