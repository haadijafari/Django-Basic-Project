from django.urls import path
from .views import *

app_name = 'index'

urlpatterns = [
    path('', mainPage, name='Travelista'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
