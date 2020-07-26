from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DAY_OF_WEEK = (
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
)


class Calendly(models.Model):
    title = models.CharField(max_length = 255)
    day = models.CharField(max_length=3, choices=DAY_OF_WEEK)
    startingTime = models.TimeField(auto_now=False, auto_now_add=False)
    endingTime = models.TimeField(auto_now=False, auto_now_add=False)
    createdAt = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)
    dateOfEvent = models.DateField(auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)