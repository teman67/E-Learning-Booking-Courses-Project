from django.shortcuts import render
from django.views.generic import TemplateView

class index(TemplateView):

    template_name='index.html'


def list_courses(request):
    
    return render(request, 'list_courses.html')


def your_view(request):
    descriptions = {
        "0": "Description of Course 0",
        "1": "Description of Course 1",
        "2": "Description of Course 2",
        "3": "Description of Course 3",
        "4": "Description of Course 4",
        "5": "Description of Course 5",
        "6": "Description of Course 6",
        "7": "Description of Course 7",
        "8": "Description of Course 8",
        "9": "Description of Course 9",
    }

    context = {'descriptions': descriptions}
    return render(request, 'list_courses.html', context)
