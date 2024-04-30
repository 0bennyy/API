from django.db import models


class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
