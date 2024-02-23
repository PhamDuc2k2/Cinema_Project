from django.db import models
from user_profile.models import Account
from event.models import Event
from movie.models import Movie 
# Create your models here.
class Ticket(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    date = models.DateTimeField(verbose_name="Ngày", auto_now_add=True)
    quantity = models.SmallIntegerField()
    total_price = models.FloatField()

    def __str__(self) -> str:
        return self.name