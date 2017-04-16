from django.db import models

# Create your models here.

from django.db import models


class Results(models.Model):
    userName = models.CharField(max_length=20)
    operator = models.IntegerField(default=0)
    average = models.FloatField(default=0.0)

    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3
    
    def __str__(self):
        return self.userName

