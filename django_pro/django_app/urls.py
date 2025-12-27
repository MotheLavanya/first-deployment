from django.urls import path
from .import views

urlpatterns=[
    path("welcome/",view=views.welcome),
    path("greetings/",view=views.greetings)
]