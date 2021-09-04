from django.db.models import fields
from django.db.models.fields import Field
from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=Todo
        fields=("id", "title", "date", "donebool", "image")
        