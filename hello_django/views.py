from django.http import HttpResponse
from django.shortcuts import render

def  hello(request):
  """
  docstring
  """
  return HttpResponse("Hello world!")

def helloView(request):
  django_name = 'django Name'
  fruit = ['西瓜', '橘子', '葡萄']
  person = {'name': 'tong', 'age': 34}
  import datetime
  now = datetime.datetime.now()
  views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
  views_num = 88
  return render(request, 'hello.html', {
    "name": django_name,
    "fruit": fruit,
    "person": person,
    "now": now,
    "views_str": views_str,
    "views_num": views_num
  })

