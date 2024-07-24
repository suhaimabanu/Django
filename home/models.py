from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    file = models.FileField()
    image = models.ImageField(null=True, blank=True)
    
class product(models.Model):
     pass  