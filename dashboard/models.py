from django.db import models

#
class Person(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return '%s %s' %(self.last_name, self.first_name)
