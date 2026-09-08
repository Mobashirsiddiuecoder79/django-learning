from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course_price(request):
    return HttpResponse("Buy My Course")