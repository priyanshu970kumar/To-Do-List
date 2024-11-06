from django.db import models

# Create your models here.

class Note_data(models.Model):
    note=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)