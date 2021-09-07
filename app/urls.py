from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutUsView.as_view(), name='aboutus'),
    path('features', views.FeaturesView.as_view(), name='features'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('signup', views.SignUpView.as_view(), name='sign_up'),
    path('signin', views.SignInView.as_view(), name='signin'),


]