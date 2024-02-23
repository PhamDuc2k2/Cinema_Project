from django.db import models
from core.models import BaseModel
from user_profile.models import Account

# Create your models here.
class Category(BaseModel):
     name = models.CharField(max_length = 100, null=False, blank=False)
     def __str__(self) -> str:
          return self.name

class Actor(BaseModel):
     name = models.CharField(max_length = 100, null=False, blank=False)
     def __str__(self) -> str:
          return self.name

class Director(BaseModel):
     name = models.CharField(max_length = 100, null=False, blank=False)
     def __str__(self) -> str:
          return self.name

class Movie(BaseModel):
    name = models.CharField(max_length = 100, null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False, default=None)
    duration_time = models.CharField(max_length=10,null=False, blank=False)
    release_day = models.DateField(null=False, blank=False)
    language = models.CharField(max_length=20, null=False, blank=False)
    trailer = models.FileField(upload_to='trailers/', verbose_name="Trailer", null=False, default=None)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    def __str__(self) -> str:
          return self.name
    

class MovieImage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/', null=False, blank=False, default=None)

class Comment(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.FloatField()