from .models import BusGateinfo, Citys, locations
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.db.models import Q

# Create your views here.


def gate(request): 
   citylists =list(Citys.objects.all())
   return render(request , 'gate.html' , { 'citylist': citylists} )


def res(request): 

    d1 = str(request.POST["desin1"])
    d2 = str(request.POST["desin2"])

    allgate = BusGateinfo.objects.all()
    cid1 = Citys.objects.get(name = d1).id
    cid2  = Citys.objects.get(name = d2).id
    all_gate1 = allgate.filter(citys = cid1)
    all_gate = all_gate1.filter(citys = cid2)
    doo = list(all_gate.filter().values_list('id', flat=True))

    #loc1 = all_gate.get("cty__loc" , city)
    ct1 = []
    ct2 = []
    for ids in all_gate:
       ct1 = ct1 + list(locations.objects.filter(gate = ids.id , city = d1))
       #ct1 = locations.objects.filter(gate = ids.id , city = d2)
    for ids in all_gate:
       ct2 = ct2+ list(locations.objects.filter(gate = ids.id , city = d2))
     
    all = zip(all_gate,ct1,ct2)
    
    #citys = [cid1 , cid2]
    #for citys_id in citys:
    #allgate = allgate.filter( citys_set__id  = citys_id)
    #gatE = BusGateinfo.objects.get(id = cid)
    #locs = locations.objects.get(gate = all_gate.id , city = 'Yangon')
    #need to get phone number

    return render(request ,'index.html', {'all' : all ,'all_gate' : all_gate , 'desin1' :d1 , 'desin2': d2 , 'ct1' :ct1 , 'ct2' :ct2})   