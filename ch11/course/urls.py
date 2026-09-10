from django.urls import path
from course.views import learn_django, html_render, fastapi

urlpatterns = [
    path("ld/", learn_django, name="learn_django"),
    path("django/", html_render, name="html_render"),
    path("api/", fastapi, name="fastapi"),
]
