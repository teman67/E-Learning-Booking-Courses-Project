from django.test import TestCase
from django.contrib.auth.models import User
from .forms import BookingForm, CourseForm, CommentForm
from .models import Booking, Course, Comment

class FormsTest(TestCase):
    def test_booking_form_valid_data(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        course = Course.objects.create(name='Test Course', description='Test Description', price=100, image_link='test.jpg')

        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'courses': [course.id],
        }

        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_booking_form_invalid_data(self):
        form_data = {
            'first_name': '',
            'last_name': '',
            'courses': [],
        }

        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_course_form_valid_data(self):
        form_data = {
            'name': 'Test Course',
            'description': 'Test Description',
            'price': 100,
            'image_link': 'test.jpg',
        }

        form = CourseForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_course_form_invalid_data(self):
        form_data = {
            'name': '',
            'description': '',
            'price': -10,  # Assuming price cannot be negative
            'image_link': 'invalid_link',
        }

        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_comment_form_valid_data(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        course = Course.objects.create(name='Test Course', description='Test Description', price=100, image_link='test.jpg')

        form_data = {
            'text': 'Test comment',
        }

        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_data(self):
        form_data = {
            'text': '',  # Assuming text cannot be empty
        }

        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
