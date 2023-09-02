from django.contrib import admin
from .models import ProductsCategory

# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('id', 'category_name', 'slug')

admin.site.register(ProductsCategory, CategoryModelAdmin)
