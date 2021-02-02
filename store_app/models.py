from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)

class Store(models.Model):
    store_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255) 
    # products = models.ManyToManyField(Product, through='Stock')

class Stock(models.Model):
    store = models.ForeignKey(Store, related_name='stock_store', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name='stock_product', on_delete = models.CASCADE) 
    qty = models.IntegerField()