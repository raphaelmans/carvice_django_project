from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name',)


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('model', 'brand', 'year')


class Rental_CarForm(forms.ModelForm):
    class Meta:
        model = Rental_Car
        # the field name should match the input name
        fields = ('fee_per_day', 'availability', 'car_id')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class ConfirmationForm(forms.ModelForm):
    class Meta:
        model = Confirmation
        fields = '__all__'


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
