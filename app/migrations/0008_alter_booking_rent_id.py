# Generated by Django 3.2.7 on 2021-10-08 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_booking_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='rent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rental_car'),
        ),
    ]
