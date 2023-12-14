from django.test import TestCase
from .forms import BookingForm, CourseForm, CommentForm
from .models import Booking, Course, Comment

class CommentFormTest(TestCase):
    def test_comment_form_valid_data(self):
        form_data = {
            'text': 'This is a valid comment.',
        }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())
