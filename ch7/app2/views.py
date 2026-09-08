from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def myapp2(request):
    return HttpResponse('App2 Page')


def app2_About(request):
    return HttpResponse('This About page of app2')