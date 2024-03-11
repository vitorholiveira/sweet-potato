from django.db import models

class Muscles(models.Model):
    name = models.CharField(max_length=100)
    muscleID= models.IntegerField()

class Exercice (models.Model):
    name = models.CharField(max_length=100)
    muscle = models.IntegerField()


instance = Muscles(name='Biceps', muscleID=1)
instance.save()