from django.db import models

# Create your models here.
class Product(models.Model):
    prodid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    price=models.FloatField()
