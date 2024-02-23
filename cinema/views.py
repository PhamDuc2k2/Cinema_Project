from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CalenderMovie
from .serializers import CalenderMovieSerializer
from rest_framework import status

# Create your views here.




class CalenderMovieViewSet(APIView):
    def get(self, request):
        queryset = CalenderMovie.objects.all()
        serializer = CalenderMovieSerializer(queryset,  many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = {
            'date' : request.data.get('date'),
            'time' : request.data.get('time')
        }
        serializer = CalenderMovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)