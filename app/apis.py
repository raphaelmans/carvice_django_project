import json
from django.forms.models import model_to_dict
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from app.models import Admin, Bill, Booking, Car, Confirmation, Rental_Car, User
from django.shortcuts import redirect, render
from django.views.generic import View
from datetime import datetime
from .forms import *


class UserByID(View):
    def get(self, request):
        user_id = request.GET.get('user_id')
        user = User.objects.get(user_id=user_id)
        return JsonResponse(model_to_dict(user))

    def put(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user_id = body['user_id']
        username = body['username']
        first_name = body['first_name']
        last_name = body['last_name']
        password = body['password']

        user = User.objects.get(user_id=user_id)

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.password = password

        user.save()
        data = {
            "status": "success"
        }
        return JsonResponse(data)

    def delete(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user_id = body['user_id']
        user = User.objects.get(user_id=user_id)
        user.delete()
        data = {
            "status": "success"
        }
        return JsonResponse(data)


class ChartData(View):
    def get(self, request):
        user_count = User.objects.all().count()
        car_count = Car.objects.all().count()
        rental_count = Rental_Car.objects.all().count()
        booking_count = Booking.objects.all().count()
        admin_count = Admin.objects.all().count()
        bill_count = Bill.objects.all().count()
        confirmation_count = Confirmation.objects.all().count()
        return JsonResponse({"user_count": user_count,
                             "rental_count": rental_count,
                             "car_count": car_count,
                             "admin_count": admin_count,
                             "bill_count": bill_count,
                             "booking_count": booking_count,
                             "confirmation_count": confirmation_count,
                             })
