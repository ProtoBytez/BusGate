
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Citys(models.Model):
    name = models.CharField(max_length=100 , null= False)
    def __str__(self):
        return self.name

class BusGateinfo(models.Model):
    gname = models.CharField(max_length= 200, null=False )

    def __str__(self):
        return self.gname
    citys = models.ManyToManyField(Citys)
    

class locations(models.Model):
    loc = models.CharField(max_length=200 , null= False)
    city = models.CharField(max_length=100 , null= False)
    ph = models.CharField(max_length=100,null= True)
    gate = models.ForeignKey(BusGateinfo, null=False , on_delete=CASCADE ,related_query_name="cty")

    def __str__(self):
        return self.gate.gname + "-----"+"["+ self.city + "]"

