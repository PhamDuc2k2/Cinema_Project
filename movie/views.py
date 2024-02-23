from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, MovieImage, Category
from .serializers import MovieSerializer, MovieImagesSerializer, MovieImagesListSerializer, CategorySerializer
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework import permissions

class MovieViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = MovieSerializer

    def get(self, request):
        query = Movie.objects.all()
        serializer = MovieSerializer(query, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
class MovieViewDetail(APIView):

    permission_classes = [permissions.IsAuthenticated]

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = MovieSerializer

    def get_object(self, movie_id):
        try:
            return Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return None
    
    def get(self, request, movie_id):
        movie_instance = self.get_object(movie_id)
        if not movie_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MovieSerializer(movie_instance)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def put(self, request, movie_id):
        movie_instance = self.get_object(movie_id)
        if not movie_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = request.data
        serializer = MovieSerializer(instance=movie_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, movie_id):
        movie_instance = self.get_object(movie_id)
        if not movie_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        movie_instance.status = False

        data = request.data
        serializer = MovieSerializer(instance=movie_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Object's status is changed to False",
                status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class MovieImagesViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = MovieImagesSerializer

    def get(self, request):
        images = MovieImage.objects.all()
        serializer = MovieImagesSerializer(images, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MovieImagesListSerializer(data=request.data)
        
        movie_id = request.data['movie']
        movie = Movie.objects.get(id=movie_id)
        files_list = request.FILES.getlist('images')
        if serializer.is_valid():
            for item in files_list:
                MovieImage.objects.create(movie=movie, images=item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CategorySerializer

    def get(self, request):
        query = Category.objects.all()
        serializer = CategorySerializer(query, many=True)
        return Response(serializer.data)
    
class CategoryViewDetail(APIView):

    permission_classes = [permissions.IsAuthenticated]

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CategorySerializer

    def get_object(self, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None
    
    def get(self, request, category_id):
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MovieSerializer(category_instance)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def put(self, request, category_id):
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = request.data
        serializer = MovieSerializer(instance=category_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )