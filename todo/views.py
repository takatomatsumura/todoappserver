from .models import Todo, TodoUser
from .serializers import TodoSerializer, TodoUserSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from django.utils import timezone
from django.utils.timezone import localtime
from django.core import serializers
import json

# Create your views here.

@api_view(["GET"])
def todolisttrue(request, uuid):
    if request.method=="GET":
        owner=TodoUser.objects.get(uuid=uuid)
        ownerserializer=TodoUserSerializer(owner, many=False)
        queryset=Todo.objects.filter(donebool=True, owner__in=ownerserializer.data["displayuser"])
        jsondata = serializers.serialize("json", queryset)
        return Response({"todo": jsondata})

@api_view(["GET"])
def todolistfalse(request, uuid):
    if request.method=="GET":
        owner=TodoUser.objects.get(uuid=uuid)
        ownerserializer=TodoUserSerializer(owner, many=False)
        queryset=Todo.objects.filter(donebool=False, owner__in=ownerserializer.data["displayuser"])
        jsondata = serializers.serialize("json", queryset)
        return Response({"todo": jsondata})

@api_view(['GET'])
def opacitylen(request, uuid):
    if request.method=="GET":
        owner=TodoUser.objects.get(uuid=uuid)
        ownerserializer=TodoUserSerializer(owner, many=False)
        queryset=Todo.objects.filter(donebool=False, date__lte=localtime(timezone.now()), owner__in=ownerserializer.data["displayuser"])
        listlen=len(queryset)
        return Response({"listlen": listlen})

class TodoRetrieveView(generics.RetrieveAPIView):
    queryset = Todo.objects.filter()
    serializer_class = TodoSerializer

class TodoCreateView(generics.CreateAPIView):
    serializer_class = TodoSerializer

class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UserList(generics.ListAPIView):
    queryset=TodoUser.objects.all()
    serializer_class = TodoUserSerializer

@api_view(["GET"])
def userretrieve(request, uuid):
    if request.method=="GET":
        if TodoUser.objects.filter(uuid=uuid).exists():
            user=TodoUser.objects.get(uuid=uuid)
            userserializer=TodoUserSerializer(user, many=False)
            return Response({"todouser": userserializer.data})
        else:
            return Response({"todouser": {"uuid": None}})

class UserCreate(generics.CreateAPIView):
    serializer_class = TodoUserSerializer

class UserUpdate(generics.UpdateAPIView):
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserSerializer

@api_view(["GET"])
def notificationtarget(request, uuid):
    if request.method=="GET":
        owner=TodoUser.objects.get(uuid=uuid)
        queryset=Todo.objects.filter(donebool=False, owner=owner)
        jsondata = serializers.serialize("json", queryset)
        return Response({"todo": jsondata})

@api_view(['GET'])
def notificationlength(request, uuid):
    if request.method=="GET":
        owner=TodoUser.objects.get(uuid=uuid)
        queryset=Todo.objects.filter(donebool=False, date__lte=localtime(timezone.now()), owner=owner)
        listlen=len(queryset)
        return Response({"listlen": listlen})
