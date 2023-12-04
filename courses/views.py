from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Course, UserProfile
from .forms import CourseForm
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Redirect to the course list page
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form})

class index(TemplateView):

    template_name='index.html'


class BookingView(View):
    def get(self, request, *args, **kwargs):
        # Your logic for handling the GET request for the booking page
        return render(request, 'booking.html')  # Replace 'booking.html' with the actual template name

    def post(self, request, *args, **kwargs):
        # Your logic for handling the POST request for the booking page
        user = request.user
        selected_courses = request.POST.getlist('courses')

        if len(selected_courses) > 3:
            messages.error(request, "You can select up to 3 courses.")
            return redirect('booking')  # Redirect back to the booking page

        booking = Booking.objects.create(user=user)
        booking.courses.set(selected_courses)

        messages.success(request, "Booking successful!")
        return redirect('booking')  # Redirect back to the booking page

@login_required
def user_profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    booked_courses = Booking.objects.filter(user=user)
    
    context = {
        'user_profile': user_profile,
        'booked_courses': booked_courses,
    }

    return render(request, 'user_profile.html', context)


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})