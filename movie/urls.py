from django.urls import path, include
from .views import MovieViewSet, MovieViewDetail, MovieImagesViewSet, CategoryViewSet

urlpatterns = [
    path('movie-view', MovieViewSet.as_view()),
    path('movie-view/<int:movie_id>/', MovieViewDetail.as_view()),

    path('movie-images-view', MovieImagesViewSet.as_view()),
    path('category-view', CategoryViewSet.as_view())
    
]