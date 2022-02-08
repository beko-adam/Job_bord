from django.core.checks import messages
from django.shortcuts import render
from .models import info

# Create your views here.

from django.core.mail import send_mail
from django.conf import settings


def contactsssss(request):
    myinfo = info.objects.first()
    if request.method == 'POST':
        subject = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
           message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
)

        print(subject, email, message)
    
 
    return render(request, 'kkk/contact.html', {"myinfo":myinfo})