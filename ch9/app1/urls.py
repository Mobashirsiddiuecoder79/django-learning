from django.urls import path
from app1.views import learn_django , home

urlpatterns = [
    path('dj/', learn_django, name = 'learn_django'),
    path('pj/', learn_django, {'status' : 'ok'}, name = 'learn_django'),
    path('', home, name = 'home'),
] 