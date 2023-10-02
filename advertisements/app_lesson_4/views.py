from django.http import HttpResponse
from django.shortcuts import render

def indexx(request):
    return HttpResponse("Домашка по 4 занятию")
# Create your views here.
