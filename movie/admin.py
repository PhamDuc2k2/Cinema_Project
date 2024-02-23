from django.contrib import admin
from django.forms import ModelChoiceField
from .models import Actor, Director, Movie, Category, Comment, MovieImage

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name', 'category', 'actor', 'director' )

class MovieImagesAdmin(admin.ModelAdmin):
    list_display = ('movie_id',)



model_admin_pairs = [
    (Actor, ActorAdmin),
    (Director, DirectorAdmin),
    (Category, CategoryAdmin),
    (Movie, MovieAdmin),
    (MovieImage, MovieImagesAdmin)
]

# Sử dụng vòng lặp để đăng ký từng cặp
for model, admin_class in model_admin_pairs:
    admin.site.register(model, admin_class)
