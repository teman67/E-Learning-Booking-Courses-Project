from django.shortcuts import render
from django.views.generic import TemplateView

class index(TemplateView):

    template_name='index.html'


def list_courses(request):
    
    return render(request, 'list_courses.html')