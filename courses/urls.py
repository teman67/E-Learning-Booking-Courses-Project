from django.urls import path
from .views import index, list_courses, your_view


urlpatterns = [
    path('', index.as_view(),name='home'),
    path('courses/', list_courses, name='courses'),
    path('your_view/', your_view, name='your_view'),
]