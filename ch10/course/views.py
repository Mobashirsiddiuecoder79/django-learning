from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. 
def learn_django(request):
    return  HttpResponse("hello django")

def html_render(request):
    return render(request,template_name='course/django.html')     

def fastapi(request):
    return render(request,template_name='course/fastapi.html')     