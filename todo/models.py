from django.db import models
import datetime

# Create your models here.


class TodoUser(models.Model):
    uuid = models.CharField(max_length=500)
    name = models.CharField(max_length=200, default="user0", blank=True, null=True)
    displayuser = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=200, default="title")
    date = models.DateTimeField(
        default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    )
    donebool = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    owner = models.ForeignKey(TodoUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ("date",)

    def __str__(self):
        return f"{self.title}(owner:{self.owner}, done:{self.donebool}, date:{self.date.strftime('%Y-%m-%d %H:%M')})"
