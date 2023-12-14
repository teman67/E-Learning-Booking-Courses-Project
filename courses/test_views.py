from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Course, Booking, UserProfile, Comment
from .forms import CourseForm, BookingForm, CommentForm

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_course_list_view(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_list.html')

    def test_add_course_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('add_course'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_course.html')

        # Test course creation
        response = self.client.post(reverse('add_course'), {
            'name': 'Test Course',
            'description': 'Test Description',
            'price': 99.99,
            'image_link': 'http://example.com/image.jpg',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertRedirects(response, reverse('course_list'))

        # Check if the course is created
        self.assertTrue(Course.objects.filter(name='Test Course').exists())

    def test_booking_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

        # Add necessary setup for booking view testing

    # Add more view tests as needed

    def test_user_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

        # Add necessary setup for user profile view testing

    def test_course_detail_view(self):
        course = Course.objects.create(
            name='Test Course',
            description='Test Description',
            price=99.99,
            image_link='http://example.com/image.jpg'
        )
        response = self.client.get(reverse('course_detail', args=[course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_detail.html')

        # Add necessary setup for course detail view testing

    # Add more view tests as needed

    def test_edit_comment_view(self):
        self.client.login(username='testuser', password='testpassword')
        comment = Comment.objects.create(
            user=self.user,
            course=Course.objects.create(
                name='Test Course',
                description='Test Description',
                price=99.99,
                image_link='http://example.com/image.jpg'
            ),
            text='Test Comment'
        )
        response = self.client.get(reverse('edit_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_comment.html')

        # Add necessary setup for edit comment view testing

    def test_delete_comment_view(self):
        self.client.login(username='testuser', password='testpassword')
        comment = Comment.objects.create(
            user=self.user,
            course=Course.objects.create(
                name='Test Course',
                description='Test Description',
                price=99.99,
                image_link='http://example.com/image.jpg'
            ),
            text='Test Comment'
        )
        response = self.client.get(reverse('delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_comment.html')

        # Add necessary setup for delete comment view testing

# Add more view tests as needed
