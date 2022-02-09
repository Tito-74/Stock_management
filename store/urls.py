from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
	path('store-list/', views.storeList, name="store-list"),
  path('store-detail/<str:pk>/', views.storeDetail, name="store-detail"),
  path('store-create/', views.storeCreate, name="store-create"),
  path('store-update/<str:pk>/', views.storeUpdate, name="store-update"),
	]