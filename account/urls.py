from django.urls import path
from .views import UserRegister



urlpatterns = [
   path('register/^admin^/danish^^/^^register/', UserRegister.as_view(), name='register'),

   ]
