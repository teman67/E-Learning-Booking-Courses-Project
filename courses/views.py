from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

class index(TemplateView):

    template_name='index.html'


def list_courses(request):
    
    return render(request, 'list_courses.html')


class BookingView(View):
    def get(self, request, *args, **kwargs):
        # Your logic for handling the GET request for the booking page
        return render(request, 'booking.html')  # Replace 'booking.html' with the actual template name

    def post(self, request, *args, **kwargs):
        # Your logic for handling the POST request for the booking page
        # This is optional, add it if your booking page handles form submissions
        pass