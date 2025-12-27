from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def welcome(req):
    return HttpResponse("Welcome to Django App...")

def greetings(req):
    return JsonResponse({"msg":"Good Morning....!"})
