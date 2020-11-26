from django.shortcuts import render, HttpResponse
from . import models

def add_book(request):
  # book = models.Book(title="菜鸟教程", price=300, publish="菜鸟出版社", pub_date="2020-10-9")
  # book.save()
  # books = models.Book.objects.create(title="如来神掌", price=190, publish="青鸟出版社", pub_date="2020-1-11")
  
  # books = models.Book.objects.all()
  books = models.Book.objects.filter(pk=2)

  for book in books:
    print(book.title)
  return HttpResponse("<p>添加数据成功</p>")
