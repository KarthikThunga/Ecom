from django.db import models

# Create your models here.

class Category(models.Model):
    c_name = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.c_name
        
class Product(models.Model):
    sizes =(
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
    )
    name = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='images', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    description = models.TextField(null=True)
    color = models.CharField(max_length=30, null=True)
    size = models.CharField(max_length=20, choices=sizes, null=True)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(max_length=10, null=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    cn_name = models.CharField(max_length=20, null=True)
    cn_email = models.EmailField(max_length=30, null=True)
    cn_description = models.TextField(null=True)
    def __str__(self):
        return self.cn_name