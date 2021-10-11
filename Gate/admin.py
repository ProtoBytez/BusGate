from django.contrib import admin
from .models import *
# Register your models here.
class LocationsAdmin(admin.ModelAdmin):
    search_fields = ('gate__gname' ,)
    list_display= ['gate' , 'city', 'loc', 'ph']
    list_filter = ['gate']

class BusGateinfoAdmin(admin.ModelAdmin):

    list_display= ['gname'  ]
    list_filter = ['gname']

admin.site.register(Citys)
admin.site.register(BusGateinfo,BusGateinfoAdmin)
admin.site.register(locations ,LocationsAdmin)
