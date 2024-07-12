from django.db import models

# Create your models here.

#models for program 3

class Fruit(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    selected = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
#models for program 5
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    text = models.TextField()
    
    def __str__(self):
        return self.name
    
class Student5(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=15)
    email = models.EmailField()
    courses = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.name