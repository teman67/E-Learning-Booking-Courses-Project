from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Course, UserProfile, Comment
from .forms import CourseForm, BookingForm, CommentForm
from django.db.models import Count
from django.db.models import Q
from django.utils import timezone
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import uuid

# HEALTH CHECK ENDPOINT - Add this to keep Supabase database active
@csrf_exempt
@require_http_methods(["GET", "POST"])
def health_check(request):
    """
    Enhanced health check endpoint that performs database operations
    to keep Supabase active and prevent auto-pause
    """
    try:
        # Multiple database operations to ensure activity
        with connection.cursor() as cursor:
            # Simple query to test connection
            cursor.execute("SELECT 1")
            
        # Count records to ensure ORM works
        total_courses = Course.objects.count()
        total_bookings = Booking.objects.count()
        total_comments = Comment.objects.count()
        total_profiles = UserProfile.objects.count()
        
        # Get latest records (if any) to test complex queries
        latest_course = Course.objects.first()
        latest_booking = Booking.objects.first()
        
        # Optional: For POST requests, perform a write operation
        activity_type = 'read_operation'
        if request.method == 'POST':
            # Test write operation by creating and deleting a dummy course
            # This ensures write access to database
            dummy_course = Course.objects.create(
                name='__health_check_dummy__',
                description='Automated health check - will be deleted',
                price=0,
                max_capacity=1
            )
            # Immediately delete to avoid clutter
            dummy_course.delete()
            activity_type = 'write_operation'
        
        return JsonResponse({
            'status': 'healthy',
            'timestamp': timezone.now().isoformat(),
            'database': {
                'total_courses': total_courses,
                'total_bookings': total_bookings,
                'total_comments': total_comments,
                'total_profiles': total_profiles,
                'latest_course_date': latest_course.created_at.isoformat() if latest_course and hasattr(latest_course, 'created_at') else None,
                'latest_booking_date': latest_booking.created_at.isoformat() if latest_booking and hasattr(latest_booking, 'created_at') else None,
                'activity_type': activity_type
            },
            'message': 'Course booking system database is active',
            'app_info': {
                'name': 'Course Booking System',
                'version': '1.0'
            }
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'error': str(e),
            'timestamp': timezone.now().isoformat(),
            'message': 'Database connection failed'
        }, status=500)


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

            # Check if any of the selected courses is already full
            for course in selected_courses:
                if course.is_full():
                    messages.error(request, f"The course {course.name} is already fully booked.")
                    return redirect('booking')

            # Check if the user has already booked 3 courses
            existing_bookings_count = (
                Booking.objects.filter(user=user)
                .values('courses')
                .annotate(course_count=Count('courses'))
                .filter(course_count__gt=0)
                .count()
            )

            total_courses_count = existing_bookings_count + len(selected_courses)

            # Check if the selected courses exceed the limit
            if len(selected_courses) > 3:
                messages.error(request, "You can select up to 3 courses.")
                return redirect('booking')

            # Check if the user booked three courses
            if total_courses_count > 3:
                messages.error(request, "You are trying to book more than 3 courses!")
                return redirect('booking')

            # Check if the user has already booked any of the selected courses
            existing_bookings = Booking.objects.filter(user=user, courses__in=selected_courses)
            if existing_bookings.exists():
                messages.error(request, "You have already booked one or more of the selected courses.")
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
    comments = Comment.objects.filter(course=course)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.course = course
            new_comment.save()
            comment_form = CommentForm()  # Clear the form after submission
    else:
        comment_form = CommentForm()

    return render(request, 'course_detail.html', {'course': course, 'comments': comments, 'comment_form': comment_form})


class EditBookingView(View):
    def get(self, request, booking_id, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        form = BookingForm(instance=booking)
        return render(request, 'edit_booking.html', {'form': form, 'booking_id': booking_id})

    def post(self, request, booking_id, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            selected_courses = form.cleaned_data['courses']

            # Check if any of the selected courses is already full
            for course in selected_courses:
                if course.is_full():
                    messages.error(request, f"The course {course.name} is already fully booked.")
                    return redirect('booking')

            # Check if the user has already booked 3 courses
            existing_bookings_count = (
                Booking.objects.filter(user=request.user)
                .exclude(id=booking_id)  # Exclude the current booking from count
                .values('courses')
                .annotate(course_count=Count('courses'))
                .filter(course_count__gt=0)
                .count()
            )

            total_courses_count = existing_bookings_count + len(selected_courses)

            if total_courses_count > 3:
                messages.error(request, "Editing this booking would exceed the limit of 3 courses.")
                return render(request, 'edit_booking.html', {'form': form, 'booking_id': booking_id})

            # Check if any of the selected courses are already booked by the user
            already_booked_courses = request.user.booking_set.exclude(id=booking_id).values_list('courses', flat=True)
            for selected_course in selected_courses:
                if selected_course.id in already_booked_courses:
                    messages.error(request, f"You have already booked the course {selected_course.name}.")
                    return render(request, 'edit_booking.html', {'form': form, 'booking_id': booking_id})

            form.save()
            messages.success(request, "Booking updated successfully.")
            return redirect('user_profile')
        else:
            messages.error(request, "Form is not valid.")
            return render(request, 'edit_booking.html', {'form': form, 'booking_id': booking_id})


class DeleteBookingView(View):
    
    def get(self, request, booking_id, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        return render(request, 'delete_booking.html', {'booking': booking})

    def post(self, request, booking_id, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return redirect('user_profile')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def search_view(request):
    query = request.GET.get('q')
    if query:
        results = Course.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        results = None

    return render(request, 'search_results.html', {'results': results, 'query': query})


def edit_comment(request, comment_id): 
    if not request.user.is_authenticated:
        return redirect('home')  # Redirect to the home page for non-authenticated users
           
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            return redirect('course_detail', course_id=comment.course.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form, 'comment_id': comment_id})

def delete_comment(request, comment_id):
    if not request.user.is_authenticated:
        return redirect('home')  # Redirect to the home page for non-authenticated users

    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    course_id = comment.course.id
    comment.delete()
    messages.success(request, "Comment deleted successfully.")
    return redirect('course_detail', course_id=course_id)
