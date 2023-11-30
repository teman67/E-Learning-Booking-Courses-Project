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


def course_detail(request, course_id):
    # Assuming you have a list of descriptions, replace this with your actual data source
    descriptions = ["Description for course 1", "Description for course 2", "3","4","5","6","7","8","9","10",]

    # Ensure course_id is a valid index
    if 0 <= course_id < len(descriptions):
        context = {
            'course_id': course_id,
            'description': descriptions[course_id],
        }
        return render(request, 'course_detail.html', context)
    else:
        # Handle invalid course_id (e.g., redirect to an error page)
        return HttpResponseNotFound("Course not found")
