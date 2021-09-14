from django.db import models
from django.db.models.base import Model

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=25)
    email_address = models.CharField(max_length=50)
    is_admin = models.BooleanField()
    
    # class meta: 
    #     db_table = 'User'

    
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    year = models.DateField()

class Rental_Car(models.Model):
    rent_id = models.AutoField(primary_key=True)
    car_id = models.ForeignKey(Car, on_delete = models.CASCADE)
    fee_per_day = models.FloatField()
    availability = models.SmallIntegerField()

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    rent_id = models.ForeignKey(Rental_Car, on_delete= models.DO_NOTHING)
    pickup_location = models.CharField(max_length=50)
    dropoff_location = models.CharField(max_length=50)
    pickup_date = models.DateField()
    dropoff_date = models.DateField()
    pickup_time = models.TimeField()
    dropoff_time = models.TimeField()
    
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Confirmation(models.Model):
    booking_id = models.ForeignKey(Booking, on_delete = models.CASCADE)
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Bill(models.Model):
    bill_no = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey(Booking, on_delete = models.DO_NOTHING)
    total_fee = models.FloatField()

