from email.policy import default
from django.db import models

class Province(models.Model):
    pCode = models.IntegerField(default='0')
    pName = models.CharField(max_length=100, default='')
    pZone = models.IntegerField(default='0')
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField()

class Amphoe(models.Model):
    aCode = models.IntegerField(default='0')
    aName = models.CharField(max_length=100, default='')
    pCode = models.IntegerField(default='0')
    pName = models.CharField(max_length=100, default='')
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField()

class Tambol(models.Model):
    tCode = models.IntegerField(default='0')
    tName = models.CharField(max_length=100, default='')
    aCode = models.IntegerField(default='0')
    aName = models.CharField(max_length=100, default='')
    pCode = models.IntegerField(default='0')
    pName = models.CharField(max_length=100, default='')
    postCode = models.IntegerField(default='0')
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField() 

class Pzone(models.Model):
    zCode = models.IntegerField(default='0')
    zName = models.CharField(max_length=100, default='')
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField()       