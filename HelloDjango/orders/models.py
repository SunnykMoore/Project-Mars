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
    SR_phone_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], null=True)
    SM_first_name = models.CharField(max_length=35)
    SM_last_name = models.CharField(max_length=35)
    SR_email = models.EmailField(max_length=254)
    department = models.CharField(max_length=20)
    physician = models.CharField(max_length=70)
    hospital = models.CharField(max_length=70)
    cust_choices = ( #Choices for the customer type dropdown menu
        ("CURRENT", "Current"),
        ("NEW", "New"),
        ("CONVERSION", "Conversion")
    )
    customer_type = models.CharField(max_length=10, choices=cust_choices, default="CURRENT")
    clinical_need = models.CharField(max_length=200)
    instrument_category = models.CharField(max_length=70)
    description = models.TextField()
    size = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(null=True)
    disclaimer = models.BooleanField()
    instrument_type= models.CharField(max_length=270)
    instrument_handle = models.CharField(max_length=270)
    status_choices = ( # Allowed status types
        ("SUBMITTED", "Submitted"),
        ("APPROVED", "Approved"),
        ("DENIED", "Denied"),
        ("IN PROGRESS", "In Progress"),
        ("SHIPPED", "Shipped"),
        ("COMPLETED", "Completed")
    )
    status = models.CharField(max_length=11, choices=status_choices, default="SUBMITTED")

    def __str__(self):
        return ("Order Number " + str(self.id))
