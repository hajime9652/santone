from django.db import models

class Tone(models.Model):
    """Holds Tone"""
    color = models.CharField(max_length=20)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class User(models.Model):
    """User for test"""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    data_joined = models.DateField()
    
# Create your models here.

