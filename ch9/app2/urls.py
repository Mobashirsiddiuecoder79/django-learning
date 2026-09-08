from django.urls import path
from app2.views import myapp2

urlpatterns = [
    path('myapp2/', myapp2 , name = 'myapp2')
] 