from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    return HttpResponse("<h1>xdd<h1>")

def vista2(request):
    return HttpResponse("<p style='color:blue'>hola<p>")
