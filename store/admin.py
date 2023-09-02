from django.contrib import admin
from .models import ProductsModel

# Register your models here.
class ProductsModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'size', 'color', 'is_available', 'created_date','modified_date')
    
admin.site.register(ProductsModel, ProductsModelAdmin)
