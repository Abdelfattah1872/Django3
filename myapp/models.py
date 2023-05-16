from django.db import models

class Student(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)