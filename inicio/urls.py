from django.urls import path
from inicio.views import index

urlpatterns = [
    path('inicio/', index),
]

