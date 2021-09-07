from django.db import models
import datetime

# Create your models here.

class TodoUser(models.Model):
    uuid=models.CharField(max_length=500)
    name=models.CharField(max_length=200, default="user0", blank=True, null=True)
    displayuser=models.ManyToManyField("self", blank=True, symmetrical=False)

class Todo(models.Model):
    title=models.CharField(max_length=200, default="title")
    date=models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    donebool=models.BooleanField(default=False) 
    image=models.TextField(blank=True, null=True)
    owner=models.ForeignKey(TodoUser, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering=("date",)