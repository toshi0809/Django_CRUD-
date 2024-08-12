from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
