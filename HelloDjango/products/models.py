from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length = 360, default = "New Product")
	description = models.TextField()
	price = models.DecimalField(max_digits=100, decimal_places=2)
	image = models.ImageField(upload_to='media', default="default.jpeg")
	part_number = models.CharField(max_length = 360, default = "X0000000")
	category_choices = (
		("CT", "Cervical/Trauma"),
		("IFAVBR", "Interbody Fusion and Vertebral Body Replacement"),
		("TC", "Thoracolumbar"),
		("MAST", "MAST"),
		("GI", "General Instruments"),
		("NP", "New Product")
	)
	category = models.CharField(max_length=6, choices=category_choices, null=True)
	size = models.CharField(max_length = 120, default = "Medium")
	handle_choices = (
		("A","1.9 Inch Ball w/ Impact Cap"),
		("B","4.8 Inch Ergonomic Inline"),
		("C","4.75 Inch Tapered w/ Impact Cap"),
		("D","6 Inch Ergonomic Inline w/ Impact Cap"),
		("E","4 Inch Cervical Inline w/Impact Cap"),
		("NP", "New Product")
	)
	handle = models.CharField(max_length=2, choices=handle_choices, null=True)
	type_choices = (
		("A", "Simple Modification - Make from Scratch"),
		("B", "Minor Mod to Standard Device"),
		("C", "Complex Design - Requires Predicate"),
		("D", "Complex Assembly - Many Components"),
		("NP", "New Product")
	)
	product_type = models.CharField(max_length=2, choices=type_choices, null=True)
	num_orders = models.PositiveIntegerField(default=0)
	department = models.CharField(max_length=20, blank=True, default='')
	
	def __str__(self):
		return (self.name)