from django.db import models

# Create your models here.
class Tree(models.Model):
    initial     = models.CharField(max_length=2)
    mostcommonname = models.CharField(max_length=50)
    scientificname = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField()
    commonname1 = models.CharField(max_length=100)
    commonname2 = models.CharField(max_length=100)
    commonname3 = models.CharField(max_length=100)
    commonname4 = models.CharField(max_length=100)