from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. 
def learn_django(request):
    return  HttpResponse("hello django")

def html_render(request):
    coursename = {'cname' : 'Django 5.1'}
    return render(request,template_name='course/django.html', context=coursename)     

def fastapi(request):
    seats = 10
    coursename = {'cname' : 'Fast API', 'username' : 'Mobashir', 'seats': seats}
    return render(request,template_name='course/fastapi.html', context=coursename)      