from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Este es el inicio de la web")


