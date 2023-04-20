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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
