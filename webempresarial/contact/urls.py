from django.urls import path
from . import views

urlpatterns = [
    #Path de la APP contact
    path('', views.contact, name='contact'),
]
