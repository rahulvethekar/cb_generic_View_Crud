from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    