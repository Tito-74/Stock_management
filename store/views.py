from django.shortcuts import render
from .serializers import StoreSerializer
from .models import Store
from rest_framework import viewsets
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# class StoreViewSet(viewsets.ModelViewSet):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer

@api_view(['GET'])
def storeList(request):
	store = Store.objects.all().order_by('-id')
	serializer = StoreSerializer(store, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def storeDetail(request, pk):
	store = Store.objects.get(id=pk)
	serializer = StoreSerializer(store, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def storeCreate(request):
	serializer = StoreSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def storeUpdate(request, pk):
	store = Store.objects.get(id=pk)
	serializer = StoreSerializer(instance=store, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


