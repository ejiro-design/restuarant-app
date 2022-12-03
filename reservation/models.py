from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Bookings(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    seats = models.IntegerField(default=0)
    date = models.DateField()
    time = models.TimeField()
    objects = UserManager()

    def __str__(self):
        return self.name + ' (' + self.email + ')'
