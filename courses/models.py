from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link = models.URLField(null=True)
    def get_course_ids(self):
        return list(Course.objects.values_list('id', flat=True))

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    # courses = models.CharField(max_length=255,null=True)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you want in the user profile
    # For example, you might want to store the user's bio, profile picture, etc.

    def __str__(self):
        return self.user.username