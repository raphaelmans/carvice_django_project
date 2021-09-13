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
    fee_per_day = models.IntegerField()
    availability = models.SmallIntegerField()



    

