from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def planes_gym(request):
    return render(request, 'planes/planes.html')