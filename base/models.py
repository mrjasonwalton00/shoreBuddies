#Models used for the Database, each model is a database table

from django.db import models
from django.contrib.auth.models import User


# Model for Buddies
class Buddies(models.Model):
    BUDDY_CHOICES = (
        ('whale', 'Whale'),
        ('turtle', 'Turtle'),
        ('dolphin', 'Dolphin'),
        ('seal', 'Seal'),
        ('seagull', 'Seagull'),
    )

    name = models.CharField(max_length=50, choices=BUDDY_CHOICES)
    picture = models.ImageField(upload_to='static/images/buddies')

    # Many-to-One relationship with User model
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    

# Model for User Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)
    age = models.IntegerField(null=True)
    profile_picture = models.ImageField(upload_to='static/images/profilePictures', null=True, blank=True)

    def __str__(self):
        return str(self.user)


