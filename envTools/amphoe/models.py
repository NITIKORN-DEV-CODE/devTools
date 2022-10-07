from django.db import models

class Amphoe(models.Model):
    aCode = models.IntegerField(default='0')
    aName = models.CharField(max_length=100, default='')
    pCode = models.IntegerField(default='0')
    pName = models.CharField(max_length=100, default='')
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField()
