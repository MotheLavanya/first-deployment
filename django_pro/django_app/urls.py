from django.urls import path
from .import views

urlpatterns=[
    path("welcome/",view=views.welcome),
    path("greetings/",view=views.greetings),
    path("reg_user/",view=views.reg_user)
]