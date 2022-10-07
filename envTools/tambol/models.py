from django.db import models

class Tambol(models.Model):
    tCode = models.IntegerField(default='0')
    tName = models.CharField(max_length=100, default='')
    aCode = models.IntegerField(default='0')
    aName = models.CharField(max_length=100, default='')
    pCode = models.IntegerField(default='0')
    pName = models.CharField(max_length=100, default='')
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField()    
