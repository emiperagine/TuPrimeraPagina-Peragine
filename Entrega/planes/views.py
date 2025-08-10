from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def planes_gym(request):
    return HttpResponse("Acá van a estar los planes disponibles")