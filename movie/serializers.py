from rest_framework import serializers
from .models import Movie, MovieImage, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
class MovieImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovieImage  
        fields = '__all__'

class MovieImagesListSerializer(serializers.Serializer):
    images = serializers.ListField(child = serializers.FileField(max_length = None, allow_empty_file=False, use_url=False))
    
    def create(self, validated_data):
        images = validated_data.pop('images')
        movie_data = validated_data.pop('movie')

        movie  = Movie.objects.create(**movie_data)

        for image in images:
            f = MovieImage.objects.create(movie=movie, images= image, **validated_data)
        return f
    
