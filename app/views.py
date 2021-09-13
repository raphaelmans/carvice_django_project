from app.models import Car, Rental_Car, User
from django.shortcuts import render
from django.views.generic import View

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
        context = {
            'user': user,
            'car': car, 
            'rental_car': rental_car, 
        }
        return render(request, 'pages/dashboard.html',context)

