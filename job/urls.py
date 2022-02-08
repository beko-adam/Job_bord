from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [

    path('', views.job_list, name='job_list' ),
    path('add', views.get_form, name='get_form'),
    path('<str:slug>', views.job_detail, name='job_detail'),
    
]
