from django.shortcuts import render
from .serializers import StoreSerializer, BookSerializer
from .models import Store, Book, Author 
from rest_framework import viewsets
from rest_framework import generics
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

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




class BookListView(generics.ListAPIView):
	serializer_class = BookSerializer
	queryset = Book.objects.all()
	filter_fields = ('title','year_of_pub')