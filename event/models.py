from django.db import models
from core.models import BaseModel
# Create your models here.
class Event(BaseModel):
    title = models.TextField(max_length=100, null=False, blank=False)
    condition = models.TextField(max_length = 100, null=False, blank=False)
    discount = models.SmallAutoField(null=False, blank=False)
    time_start = models.DateTimeField(verbose_name="Thời gian bắt đầu", null=False, blank=False)
    time_end = models.DateTimeField(verbose_name="Thời gian kết thúc", null=False, blank=False)

    def __str__(self) -> str:
        return self.title
