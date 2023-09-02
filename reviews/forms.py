from django import forms
from .models import UserReviewsModel

class ReviewForm(forms.ModelForm):
    class Meta:
        model = UserReviewsModel
        fields = ['rating', 'review']