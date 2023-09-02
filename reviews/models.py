from django.db import models
from store.models import ProductsModel
from django.contrib.auth.models import User
from django.db.models import Avg
# Create your models here.
class UserReviewsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.product.product_name} - {self.rating}'
