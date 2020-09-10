from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        subject = request.POST['Subject']
        message= request.POST['Msg']

        send_mail(
            #subject
            subject,
            # message
            'From: '+'\n'+
            'Name: ' + name + '\n' +
            'Email: '+email+'\n'+
            message
            ,
            #from_email,
            email,
            # recipientlist
            [settings.EMAIL_HOST_USER],
            # fail_silently
            fail_silently=False
        )
        return render(request,'Mail/home.html',{'name':name})
    else:
        return render(request,'Mail/home.html')
