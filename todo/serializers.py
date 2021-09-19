from .models import Todo, TodoUser
from rest_framework import serializers

# class TodoSerializer(serializers.HyperlinkedModelSerializer):

class TodoUserSerializer(serializers.ModelSerializer):
    displayuser="self"

    class Meta:
        model=TodoUser
        fields=("id", "uuid", "name", "displayuser",)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=TodoUser
        fields=("id", "uuid", "name")

class TodoGetSerializer(serializers.ModelSerializer):
    owner=UserSerializer(read_only=True)

    class Meta:
        model=Todo
        fields=("id", "title", "date", "donebool", "image", "image", "owner")

class TodoSerializer(serializers.ModelSerializer):
    owner=TodoUserSerializer

    class Meta:
        model=Todo
        fields=("id", "title", "date", "donebool", "image", "image",  "owner")