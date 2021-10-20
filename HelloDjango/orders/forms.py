from django import forms
from django.forms.models import modelformset_factory
from products.models import Product

class OrderForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label="(Nothing)")
    SR_first_name = forms.CharField(max_length=35)
    SR_last_name = forms.CharField(max_length=35)
    SR_phone_number = forms.IntegerField(max_value=9999999999)
    SM_first_name = forms.CharField(max_length=35)
    SM_last_name = forms.CharField(max_length=35)
    SR_email = forms.EmailField(max_length=254)
    department = forms.CharField(max_length=20)
    physician = forms.CharField(max_length=70)
    hospital = forms.CharField(max_length=70)
    cust_choices = ( #Choices for the customer type dropdown menu
        ("CURRENT", "Current"),
        ("NEW", "New"),
        ("CONVERSION", "Conversion")
    )
    customer_type = forms.ChoiceField(choices=cust_choices)
    clinical_need = forms.CharField(max_length=200)
    instrument_category = forms.CharField(max_length=70)
    description = forms.CharField()
    size = forms.DecimalField(max_digits=5, decimal_places=2)
    quantity = forms.IntegerField()
    disclaimer = forms.BooleanField()
    instrument_type= forms.CharField(max_length=270)
    instrument_handle = forms.CharField(max_length=270)
    status_choices = ( # Allowed status types
        ("SUBMITTED", "Submitted"),
        ("APPROVED", "Approved"),
        ("DENIED", "Denied"),
        ("IN PROGRESS", "In Progress"),
        ("SHIPPED", "Shipped"),
        ("COMPLETED", "Completed")
    )
    status = forms.ChoiceField(choices=status_choices)