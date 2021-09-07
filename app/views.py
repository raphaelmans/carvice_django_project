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


