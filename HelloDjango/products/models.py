from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.TextField()
	description = models.TextField()
	price = models.DecimalField(max_digits=100, decimal_places=2)
	image = models.ImageField(default="default.jpeg")
	product_id = models.IntegerField(default=0000)
	category = models.TextField(default = "")
