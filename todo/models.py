from django.db import models
import datetime
from django.db.models.fields import TextField

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=200, default="title")
    date=models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    donebool=models.BooleanField(default=False) 
    image=models.TextField(blank=True, null=True)

    class Meta:
        ordering=("date",)