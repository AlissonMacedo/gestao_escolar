from django.urls import path, include
from .views import Home

urlpatterns = [
    path('', Home, name='home'),
    path('index/', Home, name='home'),
    path('home/', Home, name='home'),
]
