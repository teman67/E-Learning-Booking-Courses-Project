from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Course, UserProfile
from .forms import CourseForm, BookingForm


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
        courses = Course.objects.all()
        return render(request, 'booking.html', {'courses': courses, 'form': BookingForm()})

    def post(self, request, *args, **kwargs):
        user = request.user
        form = BookingForm(request.POST)

        if form.is_valid():
            selected_courses = form.cleaned_data['courses']

            if len(selected_courses) > 3:
                messages.error(request, "You can select up to 3 courses.")
                return redirect('booking')

            booking = form.save(commit=False)
            booking.user = user
            booking.save()
            form.save_m2m()  # Save the many-to-many relationships

            messages.success(request, "Booking successful!")
            return redirect('booking')
        else:
            messages.error(request, "Form is not valid.")
            return redirect('booking')

            

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