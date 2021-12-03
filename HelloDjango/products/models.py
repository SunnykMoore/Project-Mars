from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length = 360, default = "New Product")
	description = models.TextField()
	price = models.DecimalField(max_digits=100, decimal_places=2)
	image = models.ImageField(upload_to='media', default="default.jpeg")
	part_number = models.CharField(max_length = 360, default = "X0000000")
	category_choices = (
		("Cervical/Trauma", "Cervical/Trauma"),
		("Interbody Fusion and Vertebral Body Replacement", "Interbody Fusion and Vertebral Body Replacement"),
		("Thoracolumbar", "Thoracolumbar"),
		("MAST", "MAST"),
		("General Instruments", "General Instruments"),
		("New Product", "New Product")
	)
	category = models.CharField(max_length=47, choices=category_choices, null=True)
	size = models.CharField(max_length = 120, default = "Standard")
	handle_choices = (
		("1.9 Inch Ball w/ Impact Cap","1.9 Inch Ball w/ Impact Cap"),
		("4.8 Inch Ergonomic Inline","4.8 Inch Ergonomic Inline"),
		("4.75 Inch Tapered w/ Impact Cap","4.75 Inch Tapered w/ Impact Cap"),
		("6 Inch Ergonomic Inline w/ Impact Cap","6 Inch Ergonomic Inline w/ Impact Cap"),
		("4 Inch Cervical Inline w/Impact Cap","4 Inch Cervical Inline w/Impact Cap"),
		("New Product", "New Product"),
		("Not Applicable", "Not Applicable")
	)
	handle = models.CharField(max_length=37, choices=handle_choices, null=True)
	type_choices = (
		("Simple Modification - Make from Scratch", "Simple Modification - Make from Scratch"),
		("Minor Mod to Standard Device", "Minor Mod to Standard Device"),
		("Complex Design - Requires Predicate", "Complex Design - Requires Predicate"),
		("Complex Assembly - Many Components", "Complex Assembly - Many Components"),
		("New Product", "New Product")
	)
	product_type = models.CharField(max_length=39, choices=type_choices, null=True)
	num_orders = models.PositiveIntegerField(default=0)
	department = models.CharField(max_length=20, blank=True, default='')
	
	def __str__(self):
		return (self.name)