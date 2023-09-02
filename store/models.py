from django.db import models
from category.models import ProductsCategory

# Create your models here.
class ProductsModel(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=300, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name
    
