from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.TextField()
	description = models.TextField()
	price = models.TextField()
	image = models.ImageField()
	tags = {} #potential later feature, so not all the keywors have to be in the description
