# Generated by Django 3.2.9 on 2022-03-03 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='related_Profile', serialize=False, to='auth.user')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('e_mail', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
