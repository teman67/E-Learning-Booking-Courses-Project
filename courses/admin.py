from django.contrib import admin
from .models import Course, Booking
from .forms import BookingForm

class BookingAdmin(admin.ModelAdmin):
    form = BookingForm

admin.site.register(Course)
admin.site.register(Booking, BookingAdmin)