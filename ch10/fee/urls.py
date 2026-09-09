from django.urls import path
from fee.views import student_fee

urlpatterns = [
    path('studentfee/', student_fee, name = 'student_fee')
]
