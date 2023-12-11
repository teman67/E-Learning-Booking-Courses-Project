from django.contrib import admin
from .models import Course, Booking, Comment
from .forms import BookingForm

class BookingAdmin(admin.ModelAdmin):
    form = BookingForm

admin.site.register(Course)
admin.site.register(Booking, BookingAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'text', 'created_at']
    search_fields = ['user__username', 'course__name', 'text']