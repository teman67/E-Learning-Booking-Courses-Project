from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link = models.URLField(null=True)

    def get_course_ids(self):
        return list(Course.objects.values_list('id', flat=True))

    def __str__(self):
        return self.name

    def get_booking_count(self):
        return self.booking_set.count()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255,default="") 
    last_name = models.CharField(max_length=255,default="")  
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses_booked = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()