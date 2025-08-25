from django.urls import path
from . import views

urlpatterns = [
    path('', views.planes_gym, name ="planes_gym")
]
