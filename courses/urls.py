from django.urls import path
from .views import index, list_courses, BookingView


urlpatterns = [
    path('', index.as_view(),name='home'),
    path('courses/', list_courses, name='courses'),
    path('booking/', BookingView.as_view(), name='booking'),

]