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

def featured_courses(request):
    course_ids = range(10)
    course_titles = [
        "Django with React | An Ecommerce Website",
        "Learn Ethical Hacking From Scratch",
        "The Complete Networking Fundamentals Course. Your CCNA start",
        "The Complete Python Bootcamp From Zero to Hero in Python",
        "Machine Learning A-Z™: AI, Python & R",
        "The Ultimate MySQL Bootcamp: Go from SQL Beginner to Expert",
        "Machine Learning for Absolute Beginners - Level 1",
        "The Git & Github Bootcamp",
        "230+ Exercises - Python for Data Science - NumPy + Pandas",
        "AngularJS Crash Course for Beginners",
    ]

    context = {
        'course_ids': course_ids,
        'course_titles': course_titles,
    }

    return render(request, 'featured_courses.html', context)


def course_detail(request, course_id):
    # Assuming you have a list of descriptions, replace this with your actual data source
    descriptions = ["In this course, we will build a completely customized eCommerce / shopping cart application from scratch using Django & REACT",
     "Welcome this comprehensive Ethical Hacking course! This course assumes you have NO prior knowledge! It starts with you from scratch and takes you step-by-step teaching you how to hack systems like black-hat hackers and secure them like security experts!",
      "Welcome to the Complete Network Fundamentals Course! In this course, you will learn the technologies that keep the world as you know today connected and running. We cover both the fundamentals of networking as well as the topics in the new Cisco CCNA 200-301 exam.",
      "This is the most comprehensive, yet straight-forward, course for the Python programming language on Udemy! Whether you have never programmed before, already know basic syntax, or want to learn about the advanced features of Python, this course is for you! In this course we will teach you Python 3.",
      "This course has been designed by a Data Scientist and a Machine Learning expert so that we can share our knowledge and help you learn complex theory, algorithms, and coding libraries in a simple way.",
      "This course was just completely redone and rebuilt from the ground up, with over 325 brand new videos recorded. The course now uses MySQL 8.x and covers new topics including: Window Functions, Views, and SQL modes.",
      "An excellent introduction to the topic. the lessons flowed logically and the course material was well presented. A very good course and a pleasure to take",
      "The following sentence is annoying, but also true: the best time to learn Git was yesterday. Fortunately, the second best time is today!  Git is an essential tool for work in any code-related field, from data science to game development to machine learning.  This course covers everything you need to know to start using Git and Github in the real-world today!",
      "The '230+ Exercises - Python for Data Science - NumPy + Pandas' course is an interactive, hands-on course designed for those who are seeking to gain practical experience in data science tools in Python, specifically the NumPy and Pandas libraries. The course contains over 230 exercises that provide learners with a platform to practice and consolidate their knowledge.",
      "Learn the essentials you'll need to get started with AngularJS, a popular open-source web application framework maintained by Google. During this two-hour introductory course, your instructor will introduce you to the basics of AngularJS.",]

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
