from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, Booking, UserProfile, Comment

class ModelsTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_course_model(self):
        course = Course.objects.create(
            name='Test Course',
            description='Test Description',
            price=99.99,
            image_link='http://example.com/image.jpg'
        )

        self.assertEqual(course.name, 'Test Course')
        self.assertEqual(course.get_course_ids(), [course.id])
        self.assertEqual(course.get_booking_count(), 0)
        self.assertFalse(course.is_full())

    def test_booking_model(self):
        course = Course.objects.create(
            name='Test Course',
            description='Test Description',
            price=99.99,
            image_link='http://example.com/image.jpg'
        )

        booking = Booking.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
        )
        booking.courses.add(course)

        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.first_name, 'John')
        self.assertEqual(booking.last_name, 'Doe')
        self.assertEqual(list(booking.courses.all()), [course])
        self.assertEqual(str(booking), 'John Doe')

    def test_user_profile_model(self):
        user_profile = UserProfile.objects.get(user=self.user)

        self.assertEqual(user_profile.courses_booked, 0)
        self.assertEqual(user_profile.total_price_of_booked_courses(), 0)
        self.assertEqual(str(user_profile), 'testuser')

    def test_comment_model(self):
        course = Course.objects.create(
            name='Test Course',
            description='Test Description',
            price=99.99,
            image_link='http://example.com/image.jpg'
        )

        comment = Comment.objects.create(
            user=self.user,
            course=course,
            text='This is a test comment.'
        )

        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.course, course)
        self.assertEqual(comment.text, 'This is a test comment.')
        self.assertIsNotNone(comment.created_at)

