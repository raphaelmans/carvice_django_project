from django.urls import path

from . import views
from . import apis
app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutUsView.as_view(), name='aboutus'),
    path('features', views.FeaturesView.as_view(), name='features'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('signup', views.SignUpView.as_view(), name='sign_up'),
    path('signin', views.SignInView.as_view(), name='signin'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('userregistration', views.UserRegistrationView.as_view(), name='user_registration_view'),
    path('carregistration', views.CarRegistrationView.as_view(), name='car_registration_view'),
    path('rentalcarregistration', views.RentalCarRegistrationView.as_view(), name='rentalcar_registration_view'),
    path('bookingregistration', views.BookingRegistrationView.as_view(), name='booking_registration_view'),
    path('adminregistration', views.AdminRegistrationView.as_view(), name='admin_registration_view'),
    path('confirmationregistration', views.ConfirmationRegistrationView.as_view(), name='confirmation_registration_view'),
    path('billregistration', views.BillRegistrationView.as_view(), name='bill_registartion_view'),
    path('profile', views.ProfileView.as_view(), name='profile_view'),

    # api link
    path('api/userById', apis.UserByID.as_view(), name='api_getUserById'),
    #path('api/chartData', apis.ChartData.as_view(), name='api_chartData'),
]