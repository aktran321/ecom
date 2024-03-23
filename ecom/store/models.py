from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, default = "un-branded")
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to = 'images/', null = True, blank = True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
    
    def __str__(self):
        return self.title