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
        phone_number = body['phone']
        email_address = body['email']

        user = User.objects.get(user_id=user_id)

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.password = password
        user.phone_number = phone_number
        user.email_address = email_address

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



class BookingByID(View):
    def get(self, request):
        booking_id = request.GET.get('booking_id')
        booking = Booking.objects.get(booking_id=booking_id)
        return JsonResponse(model_to_dict(booking))

        
    def put(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        booking_id = body['booking_id']
        # user_id = body['user_id']
        rent_id = Rental_Car.objects.get(rent_id=body['rent_id'])
        pickup_location = body['pickup_location']
        dropoff_location = body['dropoff_location']
        pickup_date = body['pickup_date']
        dropoff_date = body['dropoff_date']
        pickup_time = body['pickup_time']
        dropoff_time = body['dropoff_time']

        booking = Booking.objects.get(booking_id=booking_id)

        prev_rent_car = booking.rent_id
        prev_rent_car.availability = 1
        prev_rent_car.save()

        rent_id.availability = 0
        rent_id.save()

        # booking.user_id = user_id
        booking.rent_id = rent_id
        booking.pickup_location = pickup_location
        booking.pickup_location = pickup_location
        booking.dropoff_location = dropoff_location
        booking.pickup_date = pickup_date
        booking.dropoff_date = dropoff_date
        booking.pickup_time = pickup_time
        booking.dropoff_time = dropoff_time

        booking.save()
        data = {
            "status": "success"
        }
        return JsonResponse(data)

    def delete(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        booking_id = body['booking_id']
        booking = Booking.objects.get(booking_id=booking_id)

        rental_car =  booking.rent_id
        rental_car.availability = 1
        rental_car.save()

        booking.delete()
        data = {
            "status": "success"
        }
        return JsonResponse(data)

class AdminByID(View):
    def get(self, request):
        admin_id = request.GET.get('admin_id')
        admin = Admin.objects.get(admin_id=admin_id)
        return JsonResponse(model_to_dict(admin))


    def put(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        admin_id = body['admin_id']
        role = body['role']

        admin = Admin.objects.get(admin_id=admin_id)


        admin.role = role

        admin.save()

        data = {
            "status": "success"
        }
        return JsonResponse(data)

    def delete(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        admin_id = body['admin_id']
        admin = Admin.objects.get(admin_id=admin_id)
        admin.delete()
        data = {
            "status": "success"
        }
        return JsonResponse(data)

class ConfirmationByID(View):
    def get(self, request):
        booking_id = request.GET.get('booking_id')
        admin_id = request.GET.get('admin_id')
        confirmation = Confirmation.objects.get(booking_id=booking_id,admin_id=admin_id)

        return JsonResponse(model_to_dict(confirmation))

    def put(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        booking_id = body['booking_id']
        admin_id = body['admin_id']
        date = body['date']

        confirmation = Confirmation.objects.get(booking_id=booking_id,admin_id=admin_id)

        confirmation.admin_id = Admin.objects.get(admin_id=admin_id)
        confirmation.date = date

        confirmation.save()

        data = {
            "status": "success"
        }
        return JsonResponse(data)

    def delete(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        booking_id = body['booking_id']
        confirmation = Confirmation.objects.get(booking_id=booking_id)
        confirmation.delete()
        data = {
            "status": "success"
        }
        return JsonResponse(data)



class BillByID(View):
    def get(self, request):
        bill_no = request.GET.get('bill_no')
        bill = Bill.objects.get(bill_no=bill_no)

        return JsonResponse(model_to_dict(bill))

    def put(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        bill_no = body['bill_no']
        total_fee = body['total_fee']

        bill = Bill.objects.get(bill_no=bill_no)


        bill.total_fee = total_fee

        bill.save()

        data = {
            "status": "success"
        }
        return JsonResponse(data)

    def delete(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        booking_id = body['booking_id']
        confirmation = Confirmation.objects.get(booking_id=booking_id)
        confirmation.delete()
        data = {
            "status": "success"
        }
        return JsonResponse(data)

