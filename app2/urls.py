from django.urls import path 
from app2.views import * 
app_name='Any'

urlpatterns=[
    path('Bhagya/',Bhagya,name='BBhagya'),
]