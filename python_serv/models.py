from django.db import models


# Create your models here.
class PersonalData(models.Model):
    uid = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    group = models.CharField(max_length=32)
