from django.urls import path

from TestModel import views

urlpatterns = [
    path('test/model/', views.testModel)
]