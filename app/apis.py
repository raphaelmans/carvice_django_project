import json
from django.http import request, JsonResponse
from django.http.response import HttpResponse, JsonResponse
from app.models import Admin, Bill, Booking, Car, Confirmation, Rental_Car, User
from django.shortcuts import redirect, render
from django.views.generic import View
from datetime import datetime
from .forms import *
from django.contrib import messages
from django.forms.models import model_to_dict


class Login(View):

    def get(self, request):
        return JsonResponse({"message": "POST METHOD"})

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']
        data = User.objects.get(username=username, password=password)
        user_id = data.user_id
        data = {
            "user_id": user_id
        }
        return JsonResponse(data)

class UserData(View):

    def get(self, request):
        return JsonResponse({"message": "POST METHOD"})

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user_id = body['user_id']
        data = User.objects.get(user_id=user_id)
        return JsonResponse(model_to_dict(data))
