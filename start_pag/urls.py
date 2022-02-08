from django.urls import path
from . import views

app_name = 'start_pag'

urlpatterns = [

    path('', views.Home, name='home' ),

]
