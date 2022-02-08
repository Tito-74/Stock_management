from django.shortcuts import render
from .serializers import StoreSerializer
from .models import Store
from rest_framework import viewsets
# Create your views here.

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer