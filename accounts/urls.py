from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('', views.contactsssss, name='contact_us' ),

]
