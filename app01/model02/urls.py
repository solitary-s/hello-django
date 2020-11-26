from django.urls import path

from . import views

urlpatterns = [
  path('muti/', views.mutiTable),
  path('add/', views.add)
]