from django.contrib import admin
from .models import Todo, TodoUser

# Register your models here.
admin.site.register(Todo)
admin.site.register(TodoUser)
