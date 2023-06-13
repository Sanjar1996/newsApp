from django.urls import path
from .views import index, contact

urlpatterns = [
    path('', index, name='home-page'),
    path('contact/', contact, name='contact')
]
