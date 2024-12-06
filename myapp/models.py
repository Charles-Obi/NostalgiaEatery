from django.db import models

# Create your models here.
class Bookings(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    number = models.IntegerField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Register(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    file_upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.full_name

class Manager(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Orders(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    order_name = models.CharField(max_length=100)
    date = models.DateField()
    address = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name



