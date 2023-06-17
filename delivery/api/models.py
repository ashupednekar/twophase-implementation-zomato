from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=100)
    is_reserved = models.BooleanField(default=False)
    order_id = models.IntegerField(null=True)
