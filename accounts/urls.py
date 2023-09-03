from django.urls import path
from .views import userRegisterView, userLoginView, userLogoutView, updateProfile

urlpatterns = [
    path('register/', userRegisterView, name='register'),
    path('signin/', userLoginView, name='signin'),
    path('signOut/', userLogoutView, name='signOut'),
    path('profile/', updateProfile, name='profile'),
]
