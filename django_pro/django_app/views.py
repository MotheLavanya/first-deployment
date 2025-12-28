from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .serializers import CloudTableSerializer
from .models import CloudTable
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def welcome(req):
    return HttpResponse("Welcome to Django App...")

def greetings(req):
    return JsonResponse({"msg":"Good Morning....!"})

@csrf_exempt
def reg_user(req):
    user_data=json.loads(req.body)
    new_user = CloudTable.objects.create(id=user_data["id"],name=user_data["name"],email=user_data["email"],mob=user_data["mob"])
    return JsonResponse({"msg":"user created successfully.."})