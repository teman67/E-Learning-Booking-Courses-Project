from django.urls import path
from .views import *
from django.conf.urls import handler404


urlpatterns = [
    path('', index.as_view(),name='home'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('user_profile/', user_profile, name='user_profile'),
    path('courses/', course_list, name='course_list'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('edit-booking/<int:booking_id>/', EditBookingView.as_view(), name='edit_booking'),
    path('delete-booking/<int:booking_id>/', DeleteBookingView.as_view(), name='delete_booking'),
    path('edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('search/', search_view, name='search'),
]

handler404 = custom_404_view