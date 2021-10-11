from django.urls import path
from .import views

urlpatterns = [
    path('' , views.gate , name='gate' ) ,
    path('res' , views.res , name='res')
]