# Generated by Django 4.0.4 on 2022-05-04 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LogIn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='e_mail',
        ),
    ]