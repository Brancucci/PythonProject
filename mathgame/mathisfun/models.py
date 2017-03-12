from django.db import models

# Create your models here.

from django.db import models


class Results(models.Model):
    userid = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    addition = models.FloatField(default=0)
    subtraction = models.FloatField(default=0)
    multiplication = models.FloatField(default=0)
    division = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.userid

