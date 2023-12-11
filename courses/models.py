from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link = models.URLField(null=True)
    # comments = models.ManyToManyField(Comment, related_name='course_comments')

    def get_course_ids(self):
        return list(Course.objects.values_list('id', flat=True))

    def __str__(self):
        return self.name

    def get_booking_count(self):
        return self.booking_set.count()

    def is_full(self):
        return self.get_booking_count() >= 5

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

    def total_price_of_booked_courses(self):
        total_price = 0
        booked_courses = Booking.objects.filter(user=self.user)
        for booking in booked_courses:
            total_price += sum(course.price for course in booking.courses.all())
        return total_price

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"