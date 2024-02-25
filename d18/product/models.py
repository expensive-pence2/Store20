from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    desccription = models.TextField(null = True, blank = True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 256)
    desccription = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits = 123, decimal_places = 2)
    quantity = models.PositiveIntegerField(default = 0)
