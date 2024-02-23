from django.urls import path, include
from .views import CalenderMovieViewSet

urlpatterns = [
    path('calender', CalenderMovieViewSet.as_view()),
]