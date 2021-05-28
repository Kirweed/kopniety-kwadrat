from django.urls import path
from .views import allLessons, lesson

urlpatterns = [
    path('all/', allLessons, name="all_lessons"),
    path('lesson/', lesson)
]