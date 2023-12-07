from django import forms
from django.contrib.auth.models import User
from .models import Booking, Course

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'courses']
        widgets = {
            'courses': forms.CheckboxSelectMultiple,
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'price', 'image_link']
