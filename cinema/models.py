from django.db import models
from core.models import BaseModel
# Create your models here.

class CalenderMovie(BaseModel):
    date = models.DateField(verbose_name="Ngày chiếu", null=False, blank=False)
    time = models.TimeField(verbose_name="Thời gian chiếu", null=False, blank=False)


class Cinema(BaseModel):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=70)
    calender_movie = models.ForeignKey(CalenderMovie, on_delete=models.CASCADE)

class Room(BaseModel):
    total_seat = models.SmallIntegerField(null=False, blank=False)
    number = models.SmallIntegerField(null=False, blank=False)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

class Seat(BaseModel):
    type_seat = models.SmallIntegerField(null=False, blank=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


