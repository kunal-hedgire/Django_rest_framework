from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import StudDB
from .serializer import StudSerializer


class PostCreate(generics.CreateAPIView):
    queryset = StudDB.objects.all()
    serializer_class=StudSerializer


class PostDelete(generics.DestroyAPIView):
    queryset = StudDB.objects.all()
    serializer_class = StudSerializer
    


class PostList(generics.ListAPIView):
    queryset = StudDB.objects.all()
    serializer_class = StudSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = StudDB.objects.all()
    serializer_class = StudSerializer


class PostUpdate(generics.UpdateAPIView):
    queryset = StudDB.objects.all()
    serializer_class = StudSerializer




