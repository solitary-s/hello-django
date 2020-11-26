from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def mutiTable(reqeust):
  return HttpResponse("121212")

def add(reqeust):
  pub_obj = models.Publish.objects.filter(pk=1).first()
  book = models.Book.objects.create(title="菜鸟教程", price="200", pub_date="2020-10-10", publish=pub_obj)
  print(book, type(book))
  return HttpResponse(book)