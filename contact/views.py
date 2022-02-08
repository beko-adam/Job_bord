from typing import Reversible
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .form import SignupForm, User_Form, Porfile_Form
from .models import Profile

# Create your views here.

def signup(request):
    
    if request.method=='POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)

            return redirect('/account/profile')
    else:

        form = SignupForm()

    return render(request, 'registration/signup.html', {'form':form})




def profiles(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'account/profile.html', {'profile':profile})


def profile_edit(request):
    pofile = Profile.objects.get(user=request.user) 

    if request.method == 'POST':
       userform = User_Form(request.POST, instance=request.user)
       profileform = Porfile_Form(request.POST, request.FILES, instance=pofile)

       if userform.is_valid() and profileform.is_valid():
           userform.save()
           myprofileform = profileform.save(commit=False)
           myprofileform.user = request.user
           myprofileform.save()

           return redirect('/accounts/profile')

    else:
        userform = User_Form(instance=request.user)
        profileform = Porfile_Form(instance=pofile)


    return render(request, 'account/profile_edit.html', {'userform':userform, 'profileform':profileform})


