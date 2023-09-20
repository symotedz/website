from django.db import models

# Create your models here.

class Enquiry(models.Model):
    PRODUCT_CHOICES = (
        ('symotedz Analytics', 'Symotedz Analytics'),
        ('Symotedz bulk server', 'Symotedz bulk server'),
        ('Symoted appointment booking system', 'Symotedz appointment booking system'),
        ('Symotedz ISP system', 'Symotedz isp system'),
        ('Symotedz HR,Payroll & Accounting System', 'Symotedz HR,Payroll & Accounting system'),
    )
    
    first_name = models.CharField(max_length=255)
    Email = models.EmailField()
    Product = models.CharField(max_length=255, choices = PRODUCT_CHOICES)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    enquiry = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
