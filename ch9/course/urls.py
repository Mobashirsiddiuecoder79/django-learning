from django.contrib import admin
from django.urls import path
from course.views import course_price

urlpatterns = [
    path('courseprice/', course_price , name='courseprice')
]