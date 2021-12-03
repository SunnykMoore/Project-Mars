from django.db import models
from django.core.validators import MaxValueValidator
from products import models as product_models
from django.core.exceptions import ValidationError

# Create your models here.

class Order(models.Model):
    def validate_true(value):
        if value is False:
            raise ValidationError("You must accept the disclaimer to submit the order.")

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
		("Cervical/Trauma", "Cervical/Trauma"),
		("Interbody Fusion and Vertebral Body Replacement", "Interbody Fusion and Vertebral Body Replacement"),
		("Thoracolumbar", "Thoracolumbar"),
		("MAST", "MAST"),
		("General Instruments", "General Instruments"),
		("New Product", "New Product")
	)
    instrument_category = models.CharField(max_length=47, choices=category_choices, null=True)
    description = models.TextField()
    size = models.CharField(max_length = 120, default = "Standard")
    quantity = models.PositiveIntegerField()
    type_choices = (
		("Simple Modification - Make from Scratch", "Simple Modification - Make from Scratch"),
		("Minor Mod to Standard Device", "Minor Mod to Standard Device"),
		("Complex Design - Requires Predicate", "Complex Design - Requires Predicate"),
		("Complex Assembly - Many Components", "Complex Assembly - Many Components"),
		("New Product", "New Product")
	)
    instrument_type = models.CharField(max_length=39, choices=type_choices, null=True, help_text=
        ("Simple Modification - Make from Scratch: $750-1250. "
        "Minor Mod to Standard Device: $1000-$2000. "
        "Complex Design - Requires Predicate: $1750-$3000. "
        "Complex Assembly - Many Components: $3000-$4500."))
    handle_choices = (
		("1.9 Inch Ball w/ Impact Cap","1.9 Inch Ball w/ Impact Cap"),
		("4.8 Inch Ergonomic Inline","4.8 Inch Ergonomic Inline"),
		("4.75 Inch Tapered w/ Impact Cap","4.75 Inch Tapered w/ Impact Cap"),
		("6 Inch Ergonomic Inline w/ Impact Cap","6 Inch Ergonomic Inline w/ Impact Cap"),
		("4 Inch Cervical Inline w/Impact Cap","4 Inch Cervical Inline w/Impact Cap"),
		("New Product", "New Product"),
		("Not Applicable", "Not Applicable")
	)
    instrument_handle = models.CharField(max_length=37, choices=handle_choices, null=True)
    disclaimer = models.BooleanField(validators=[validate_true], help_text=
        "I agree to submit this request form to my manager for approval.  If actual cost exceeds maximum price range, I will be notified with adjusted price prior to manufacturing with no obligation to continue.")
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