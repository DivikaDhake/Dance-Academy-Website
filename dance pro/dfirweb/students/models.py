# students/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)  # Add this field
    age = models.IntegerField()
    style = models.CharField(max_length=50)
    date = models.DateField()
    state = models.CharField(max_length=50)
    email = models.EmailField(default='noemail@example.com')

    def __str__(self):
        return self.name
