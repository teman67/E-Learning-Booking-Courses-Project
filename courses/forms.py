from django import forms
from django.contrib.auth.models import User
from .models import Booking, Course

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['courses']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'price']
