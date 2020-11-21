from django.http import HttpResponse

from TestModel.models import Test

def testdb(request):
  test1 = Test(name = "aloneness")
  test1.save()
  return HttpResponse("<p>HELLO, 数据添加成功！</p>" + test1.name)

def getdb(request):
  response = ''
  list = Test.objects.all()
  for var in list:
    response += var.name + " "
  return HttpResponse("<p>" + response + "</p>")

def updatedb(request):
  test1 = Test.objects.get(id=1)
  test1.name = 'orange'
  test1.save()

  # Test.objects.filter(id=1).update(name='orange')

  return HttpResponse("<p>修改成功</p>")

def deletedb(request):
  test1 = Test.objects.get(id=1)
  test1.delete()
  return HttpResponse("<p>删除成功</p>")