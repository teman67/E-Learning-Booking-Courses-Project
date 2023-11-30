from django.urls import path
from .views import index, list_courses, BookingView, course_detail


urlpatterns = [
    path('', index.as_view(),name='home'),
    path('courses/', list_courses, name='courses'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
]