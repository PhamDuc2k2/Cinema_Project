from django.contrib import admin
from .models import CalenderMovie, Cinema, Room, Seat

# Register your models here.
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

class CalenderMovieAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'status')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'total_seat', 'status')

class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'room')

model_admin_pairs = [
    (Seat, SeatAdmin),
    (Room, RoomAdmin),
    (Cinema, CinemaAdmin),
    (CalenderMovie, CalenderMovieAdmin),
]

# Sử dụng vòng lặp để đăng ký từng cặp
for model, admin_class in model_admin_pairs:
    admin.site.register(model, admin_class)
# admin.site.register((Seat, Room, Cinema, CalenderMovie), SeatAdmin, RoomAdmin, CinemaAdmin, CalenderMovie)

