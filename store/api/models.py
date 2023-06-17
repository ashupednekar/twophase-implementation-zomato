from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)


class Package(models.Model):
    is_reserved = models.BooleanField(default=False)
    order_id = models.IntegerField(null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)



