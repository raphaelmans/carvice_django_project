from django.http import request
from django.http.response import HttpResponse, JsonResponse
from app.models import Admin, Bill, Booking, Car, Confirmation, Rental_Car, User
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import *
from django.contrib import messages

class IndexView(View):
    def get(self, request):
        return render(request, 'pages/index.html',{})


class AboutUsView(View):
    
    def get(self,request):
        return render(request, 'pages/about_us.html',{})


class FeaturesView(View):
    
    def get(self,request):
        return render(request, 'pages/features.html',{})

        
class ContactView(View):
    
    def get(self,request):
        return render(request, 'pages/contact.html',{})

class SignUpView(View):
    
    def get(self,request):
        return render(request, 'pages/signup.html',{})


class SignInView(View):
    
    def get(self,request):
        return render(request, 'pages/signin.html',{})

class DashboardView(View):
    
    def get(self,request):
        user = User.objects.all()
        car = Car.objects.all()
        rental_car = Rental_Car.objects.all()
        booking = Booking.objects.all()
        confirmation = Confirmation.objects.all()
        bill = Bill.objects.all()
        admin = Admin.objects.all()
        context = {
            'user': user,
            'car': car, 
            'rental_car': rental_car, 
            'booking': booking, 
            'confirmation': confirmation, 
            'bill': bill, 
            'admin': admin, 
        }
        return render(request, 'pages/admin/dashboard.html',context)

class UserRegistrationView(View): 
    def get(self,request):
        return render(request, 'pages/admin/insert_user.html',{})
    
    def post(self,request):
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
            form = Car(model = ml, brand = bd, year = yr) 
            form.save()

            return redirect('app:dashboard')
        
        else:
            print(form.errors)
            return HttpResponse('not valid')

class RentalCarRegistrationView(View): 
    def get(self,request):
        car = Car.objects.all()
        context = {
            'car': car, 
        }
        return render(request, 'pages/admin/insert_rentalcar.html', context)

    def post(self,request):
        form = Rental_CarForm(request.POST)

        if form.is_valid():
            car = Car.objects.get(car_id = request.POST.get("car_id")) #returning the car instance
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

