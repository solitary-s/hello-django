from django.db import models

# Create your models here.
class Test(models.Model):
  """
  docstring
  """
  name = models.CharField(max_length=20)