from django.http import HttpResponse

from TestModel.models import Test

def testdb(request):
  test1 = Test(name = "solitary")
  test1.save()
  return HttpResponse("<p>HELLO, 数据添加成功！</p>" + test1.name)