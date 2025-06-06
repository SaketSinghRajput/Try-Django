from django.db import models

# Create your models here.
class Article(models.Model):
    
    title           = models.CharField(max_length=120, ) # max_lenght = rquired
    description     = models.TextField(blank=True, null=True)
    # image           = models.ImageField(upload_to='images/', blank=True, null=True)
    published       = models.BooleanField(default=True)
