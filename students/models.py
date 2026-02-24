

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
