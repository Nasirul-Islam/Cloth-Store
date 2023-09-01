from django.urls import path
from .views import userRegisterView, userLoginView, userLogoutView, dashbord

urlpatterns = [
    path('register/', userRegisterView, name='register'),
    path('signin/', userLoginView, name='signin'),
    path('signOut/', userLogoutView, name='signOut'),
    path('dashbord/', dashbord, name='dashbord'),
]
