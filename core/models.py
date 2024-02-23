from django.db import models
# Create your models here.

class BaseModel(models.Model):
    class Meta:
        abstract=True
    created_date = models.DateTimeField(verbose_name="Ngày khởi tạo", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Ngày cập nhật", auto_now=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

