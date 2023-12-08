from django.urls import path
from app1.views import *
app_name='some'

urlpatterns=[
    path('Venkey/',Venkey,name='Venkey'),
]