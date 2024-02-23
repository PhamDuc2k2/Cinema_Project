from rest_framework import serializers
from .models import Cinema, Seat, Room, CalenderMovie

class CalenderMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalenderMovie
        fields = '__all__'

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'