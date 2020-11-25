from django.shortcuts import render
from django.http import HttpResponse



def testModel (request):
  return HttpResponse("hello testModel")