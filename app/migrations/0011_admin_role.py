# Generated by Django 3.2.7 on 2021-10-13 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_confirmation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='role',
            field=models.CharField(default='STAFF', max_length=25),
        ),
    ]