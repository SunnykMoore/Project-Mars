from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length = 360, default = "New Product")
	description = models.TextField()
	price = models.DecimalField(max_digits=100, decimal_places=2)
	image = models.ImageField(upload_to='media', default="default.jpeg")
	product_id = models.IntegerField(default=0000)
	category_choices = (
		("CT", "Cervical/Trauma"),
		("IFAVBR", "Interbody Fusion and Vertebral Body Replacement"),
		("TC", "Thoracolumbar"),
		("MAST", "MAST"),
		("GI", "General Instruments")
	)
	category = models.CharField(max_length=6, choices=category_choices, null=True)
	size = models.CharField(max_length = 120, default = "Medium")
	handle = models.CharField(max_length = 360, default = "None")
	product_type = models.CharField(max_length = 120, default = "Regular")
	num_orders = models.PositiveIntegerField(default=0)
	department = models.CharField(max_length=20, null=True)
	
	def __str__(self):
		return (self.name)