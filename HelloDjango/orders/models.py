from django.db import models
from django.core.validators import MaxValueValidator
from products import models as product_models

# Create your models here.

class Order(models.Model):
    product = models.ForeignKey(
        product_models.Product,
        on_delete=models.SET_NULL,
        null=True
    )
    SR_first_name = models.CharField(max_length=35)
    SR_last_name = models.CharField(max_length=35)
    SR_phone_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    SM_first_name = models.CharField(max_length=35)
    SM_last_name = models.CharField(max_length=35)
    SR_email = models.EmailField(max_length=254)
    physician = models.CharField(max_length=70)
    hospital = models.CharField(max_length=70)
    cust_choices = ( #Choices for the customer type dropdown menu
        ("CURRENT", "Current"),
        ("NEW", "New"),
        ("CONVERSION", "Conversion")
    )
    customer_type = models.CharField(max_length=10, choices=cust_choices, default="CURRENT")
    clinical_need = models.CharField(max_length=200)
    category_choices = (
		("CT", "Cervical/Trauma"),
		("IFAVBR", "Interbody Fusion and Vertebral Body Replacement"),
		("TC", "Thoracolumbar"),
		("MAST", "MAST"),
		("GI", "General Instruments"),
		("NP", "New Product")
	)
    instrument_category = models.CharField(max_length=6, choices=category_choices, null=True)
    description = models.TextField()
    size = models.CharField(max_length = 120, default = "Standard")
    quantity = models.PositiveIntegerField()
    disclaimer = models.BooleanField()
    type_choices = (
		("A", "Simple Modification - Make from Scratch"),
		("B", "Minor Mod to Standard Device"),
		("C", "Complex Design - Requires Predicate"),
		("D", "Complex Assembly - Many Components"),
		("NP", "New Product")
	)
    instrument_type = models.CharField(max_length=2, choices=type_choices, null=True)
    handle_choices = (
		("A","1.9 Inch Ball w/ Impact Cap"),
		("B","4.8 Inch Ergonomic Inline"),
		("C","4.75 Inch Tapered w/ Impact Cap"),
		("D","6 Inch Ergonomic Inline w/ Impact Cap"),
		("E","4 Inch Cervical Inline w/Impact Cap"),
		("NP", "New Product"),
		("NA", "Not Applicable")
	)
    instrument_handle = models.CharField(max_length=2, choices=handle_choices, null=True)
    status_choices = ( # Allowed status types
        ("SUBMITTED", "Submitted"),
        ("APPROVED", "Approved"),
        ("DENIED", "Denied"),
        ("IN PROGRESS", "In Progress"),
        ("SHIPPED", "Shipped"),
        ("COMPLETED", "Completed")
    )
    status = models.CharField(max_length=11, choices=status_choices, default="SUBMITTED")
    is_reordered = models.BooleanField(default=False)
    num_reorders = models.PositiveIntegerField(default=0)
    parent_reorder = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, default=None)
    denial_reason = models.TextField(default = "")

    def __str__(self):
        return ("Order Number " + str(self.id))
