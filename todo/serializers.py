from django.db.models import fields
from django.db.models.fields import Field
from .models import Todo, TodoUser
from rest_framework import serializers

# class TodoSerializer(serializers.HyperlinkedModelSerializer):

class TodoUserSerializer(serializers.ModelSerializer):
    displayuser="self"

    class Meta:
        model=TodoUser
        fields=("id", "uuid", "name", "displayuser",)

class TodoSerializer(serializers.ModelSerializer):
    owner=TodoUserSerializer

    class Meta:
        model=Todo
        fields=("id", "title", "date", "donebool", "image", "owner",)