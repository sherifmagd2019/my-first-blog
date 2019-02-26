# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Department (models.Model):
    department = models.TextField(  null=True, blank=True)

    def __str__(self):
        return self.department

class CustomUser(AbstractUser):
    # add additional fields in here
    department = models.ForeignKey(Department,related_name='ttt',on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return   self.username
    
    def get1(self):
        d=""
        return d