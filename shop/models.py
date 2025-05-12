from django.db import models
from django.conf.urls.static import static 

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=300, null=True)
    price = models.IntegerField(max_length=12)
    picture = models.ImageField(upload_to='upload/product/', height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name