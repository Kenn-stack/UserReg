from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, related_name= 'related_Profile' , on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    date_created = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return '%s %s' %(self.firstname, self.lastname)


