from django import forms
from .models import * 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class Rental_CarForm(forms.ModelForm):
    class Meta:
        model = Rental_Car
        fields = '__all__'

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