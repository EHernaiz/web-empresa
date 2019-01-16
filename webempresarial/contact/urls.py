from django.urls import path
from . import views

urlpatterns = [
    #Path de la APP contact
    path('contact/', views.contact, name='contact'),
]
