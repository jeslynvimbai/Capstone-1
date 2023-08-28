from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BandMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='band_members/')

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    tickets_available = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField() 

    def __str__(self):
        return self.user.username