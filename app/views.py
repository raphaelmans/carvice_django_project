from app.models import Admin, Bill, Booking, Car, Confirmation, Rental_Car, User
from django.shortcuts import render
from django.views.generic import View
from .forms import *

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
        return render(request, 'pages/dashboard.html',context)

