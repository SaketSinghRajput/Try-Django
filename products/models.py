from django.db import models

# Create your models here.
class Products(models.Model):
    
    title           = models.CharField(max_length=120, ) # max_lenght = rquired
    description    = models.TextField(blank=True, null=True)
    price           = models.DecimalField(max_digits=100, decimal_places=2)
    summary         = models.TextField(default='this is cool!')
    featured        = models.BooleanField(default=True)