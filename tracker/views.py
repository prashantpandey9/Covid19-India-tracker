from django.shortcuts import render
import requests
import json
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    if request.method=="POST":
        message=request.POST["message"]
        send_mail(
            name,
            message+" feedback from "+ mail,
            settings.EMAIL_HOST_USER,
            ["prashantpandey94551@gmail.com","radhasati2019@gmail.com","rajattiwari785@gmail.com"],
            fail_silently="False")
    return render(request,"contact.html")


def apiforindia():
    api="https://api.covid19india.org/data.json"

    s=(requests.get(api)).text

    data=json.loads(s)
    b=1
    return data

def apiforworld():
    api="https://corona.lmao.ninja/v2/all"
    s=(requests.get(api)).text
    data=json.loads(s)
    return data

def country():
    api="https://corona.lmao.ninja/v2/countries#"

    s=(requests.get(api)).text

    data=json.loads(s)
    return data
    
# Create your views here.
def Track(request):
    parms={
        "data":apiforindia(),
        "data2":apiforworld(),
    }
    return render(request, 'main.html', parms)

def globalD(request):
    parms={
        "data1":country(),
        "data":apiforindia(),
        "data2":apiforworld(),
    }
    return render(request, 'global.html', parms)

def image(request):
    parms={
    }
    return render(request, 'coro.html', parms)
