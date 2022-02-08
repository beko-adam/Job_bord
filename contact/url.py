from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [

    path('signup', views.signup, name='signup'),
    path('profile', views.profiles, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),

    
]