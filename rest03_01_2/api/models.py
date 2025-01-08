from django.db import models

# Create your models here.
class Marks(models.Model):
    rollno=models.IntegerField()
    sub1=models.IntegerField()
    sub2=models.IntegerField()
    