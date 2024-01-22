from django.db import models


class Booking(models.Model):
   """
   Represents a booking made by a guest at the restaurant.
   """
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


class Menu(models.Model):
   """
   Represents a menu item in a restaurant.
   """
   name = models.CharField(max_length=200)
   price = models.IntegerField(null=False)
   menu_item_description = models.TextField(max_length=1000, default='')

   def __str__(self):
      return self.name
