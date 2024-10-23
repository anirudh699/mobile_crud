from django.db import models

# Create your models here.
class Mobiles(models.Model):
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    release_year=models.IntegerField()
    price=models.PositiveIntegerField()
    