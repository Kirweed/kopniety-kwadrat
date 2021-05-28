from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@staff_member_required
def createLesson(request):
    return render(request, 'create-lesson.html')

def mainPage(request):
    return render(request, 'index.html')

def allLessons(request):
    return render(request, 'all.html')

def lesson(request):
    return render(request, 'lesson.html')