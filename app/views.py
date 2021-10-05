from django.http import request
from django.http.response import HttpResponse, JsonResponse
from app.models import Admin, Bill, Booking, Car, Confirmation, Rental_Car, User
from django.shortcuts import redirect, render
from django.views.generic import View
from datetime import datetime
from .forms import *
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        return render(request, 'pages/index.html', {})


class AboutUsView(View):

    def get(self, request):
        return render(request, 'pages/about_us.html', {})


class FeaturesView(View):

    def get(self, request):
        return render(request, 'pages/features.html', {})


class ContactView(View):

    def get(self, request):
        return render(request, 'pages/contact.html', {})


class SignUpView(View):

    def get(self, request):
        return render(request, 'pages/signup.html', {})

    def post(self, request):
            form = UserForm(request.POST)

            if form.is_valid():
                fname = request.POST.get("first_name")
                lname = request.POST.get("last_name")
                un = request.POST.get("username")
                pw = request.POST.get("password")
                
                #username filtering
                if(User.objects.filter(username = un).exists()):
                    messages.error(request, "Username already exists")
                    # return HttpResponse('not valid')
                    return redirect('app:sign_up') 

                else: 
                    form = User(username = un, password = pw,first_name = fname, last_name = lname, is_admin=0) 
                    form.save()
                    return redirect('app:index')
            
            else:
                print(form.errors)


class SignInView(View):

    def get(self, request):
        return render(request, 'pages/signin.html', {})


class DashboardView(View):

    def get(self, request):
        user = User.objects.all()
        car = Car.objects.all()
        rental_car = Rental_Car.objects.all()
        booking = Booking.objects.all()
        confirmation = Confirmation.objects.all()
        bill = Bill.objects.all()
        admin = Admin.objects.all()
        user_count = User.objects.all().count()
        car_count = Car.objects.all().count()
        rental_count = Rental_Car.objects.all().count()
        booking_count = Booking.objects.all().count()
        admin_count = Admin.objects.all().count()
        bill_count = Bill.objects.all().count()
        confirmation_count = Confirmation.objects.all().count()
        context = {
            'user': user,
            'car': car,
            'rental_car': rental_car,
            'booking': booking,
            'confirmation': confirmation,
            'bill': bill,
            'admin': admin,
            "user_count": user_count,
            "rental_count": rental_count,
            "car_count": car_count,
            "admin_count": admin_count,
            "bill_count": bill_count,
            "booking_count": booking_count,
            "confirmation_count": confirmation_count,
        }
        return render(request, 'pages/admin/dashboard.html', context)

  
        
    
    




class UserRegistrationView(View):
    def get(self, request):
        return render(request, 'pages/admin/insert_user.html', {})

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            fname = request.POST.get("first_name")
            lname = request.POST.get("last_name")
            un = request.POST.get("username")
            pw = request.POST.get("password")
            email = request.POST.get("email_address")
            phone = request.POST.get("phone_number")
            
            #username filtering
            if(User.objects.filter(username = un).exists()):
                messages.error(request, "Username already exists")
                return redirect('app:user_registration_view') 

            else: 
                form = User(username = un, password = pw,first_name = fname, last_name = lname,  phone_number = phone, email_address = email, is_admin=0) 
                form.save()
                return redirect('app:dashboard')
        
        else:
            print(form.errors)
            return HttpResponse('not valid')



class CarRegistrationView(View): 
    def get(self,request):
        return render(request, 'pages/admin/insert_car.html',{})
    
    def post(self,request):
        form = CarForm(request.POST)

        if form.is_valid():
            ml = request.POST.get("model")
            bd = request.POST.get("brand")
            yr = request.POST.get("year")
            form = Car(model=ml, brand=bd, year=yr)
            form.save()

            return redirect('app:dashboard')

        else:
            print(form.errors)
            return HttpResponse('not valid')


class RentalCarRegistrationView(View):
    def get(self, request):
        car = Car.objects.all()
        context = {
            'car': car,
        }
        return render(request, 'pages/admin/insert_rentalcar.html', context)

    def post(self, request):
        form = Rental_CarForm(request.POST)

        if form.is_valid():
            car = Car.objects.get(car_id=request.POST.get(
                "car_id"))  # returning the car instance
            avail = request.POST.get("availability")
            fee = request.POST.get("fee_per_day")
            
            #If car instance is present in the database 
            if(Rental_Car.objects.filter(car_id = car).exists()):
                messages.error(request, "Car already exists")
                return redirect('app:rentalcar_registration_view')

            else: 
                form = Rental_Car(car_id = car, availability = avail, fee_per_day = fee) 
                form.save()
                return redirect('app:dashboard')
        
        else:
            print(form.errors)
            return HttpResponse('not valid')

class BookingRegistrationView(View):
    def get(self, request):
        user = User.objects.all()
        rental_car = Rental_Car.objects.select_related('car_id').all()
        context = {
            'user': user,
            'rental_car': rental_car,
        }
        return render(request, 'pages/admin/insert_booking.html', context)

    def post(self, request):
        form = BookingForm(request.POST)

        if form.is_valid():
            user_id = User.objects.get(user_id=request.POST.get("user_id"))
            car = Rental_Car.objects.get(rent_id=request.POST.get("rent_id"))
            pickup_location = request.POST.get("pickup_location")
            dropoff_location = request.POST.get("dropoff_location")
            pickup_date = request.POST.get("pickup_date")
            dropoff_date = request.POST.get("dropoff_date")
            pickup_time = request.POST.get("pickup_time")
            dropoff_time = request.POST.get("dropoff_time")

            object = Booking(rent_id=car,
                             user_id=user_id,
                             pickup_location=pickup_location,
                             dropoff_location=dropoff_location,
                             pickup_date=pickup_date,
                             dropoff_date=dropoff_date,
                             pickup_time=pickup_time,
                             dropoff_time=dropoff_time,
                             )
            object.save()

            return redirect('app:dashboard')
        else:
            print(form.errors)
            return HttpResponse('not valid')


class AdminRegistrationView(View):
    def get(self, request):
        user = User.objects.all()
        context = {
            'user': user,
        }
        return render(request, 'pages/admin/insert_admin.html', context)

    def post(self, request):
        form = AdminForm(request.POST)

        if form.is_valid():
            user_id = User.objects.get(user_id=request.POST.get("user_id"))

            object = Admin(
                user_id=user_id,
            )
            object.save()

            return redirect('app:dashboard')
        else:
            print(form.errors)
            return HttpResponse('not valid')


class ConfirmationRegistrationView(View):
    def get(self, request):
        admins = Admin.objects.all()
        bookings = Booking.objects.all()
        context = {
            'bookings': bookings,
            'admins': admins,
        }
        return render(request, 'pages/admin/insert_confirmation.html', context)

    def post(self, request):
        form = ConfirmationForm(request.POST)

        if form.is_valid():
            booking_id = Booking.objects.get(
                booking_id=request.POST.get("booking_id"))
            admin_id = Admin.objects.get(admin_id=request.POST.get("admin_id"))

            object = Confirmation(
                booking_id=booking_id,
                admin_id=admin_id,
            )
            object.save()

            return redirect('app:dashboard')
            
        else:
            print(form.errors)
            return HttpResponse('not valid')


class BillRegistrationView(View):
    def get(self, request):
        bookings = Booking.objects.all()
        context = {
            'bookings': bookings,
        }
        return render(request, 'pages/admin/insert_bill.html', context)

    def post(self, request):
        form = BillForm(request.POST)

        if form.is_valid():
            booking_id = Booking.objects.get(
                booking_id=request.POST.get("booking_id"))
            total_fee = request.POST.get("total_fee")
            object = Bill(
                booking_id=booking_id,
                total_fee=total_fee,
            )
            object.save()

            return redirect('app:dashboard')

        else:
            print(form.errors)
            return HttpResponse('not valid')
