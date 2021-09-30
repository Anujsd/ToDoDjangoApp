from django.db import models

# Create your models here.
class User(models.Model):
    task_name=models.CharField(max_length=50)
    task_desc=models.TextField(max_length=150)
