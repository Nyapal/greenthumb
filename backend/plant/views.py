from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets 
from .serializers import PlantSerializer
from .models import Plant 

class PlantView(viewsets.ModelViewSet):
  serializer_class = PlantSerializer
  queryset = Plant.objects.all()
