
from django.db import models

# Create your models here.
class servicemodule(models.Model):
    name=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    desc=models.TextField()

  