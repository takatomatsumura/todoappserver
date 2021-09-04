from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from django.utils import timezone
from django.utils.timezone import localtime

# Create your views here.

class RetrieveView(generics.RetrieveAPIView):
    queryset = Todo.objects.filter()
    serializer_class = TodoSerializer

class ListViewBoolFalse(generics.ListAPIView):
    queryset=Todo.objects.filter(donebool=False)
    serializer_class = TodoSerializer

@api_view(['GET'])
def listlength(request):
    if request.method=="GET":
        queryset=Todo.objects.filter(donebool=False, date__lte=localtime(timezone.now()))
        listlen=len(queryset)
        return Response({"listlen": listlen})

class ListViewBoolTrue(generics.ListAPIView):
    queryset=Todo.objects.filter(donebool=True)
    serializer_class = TodoSerializer

class CreateView(generics.CreateAPIView):
    serializer_class = TodoSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
