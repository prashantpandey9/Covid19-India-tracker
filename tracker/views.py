from django.shortcuts import render
import requests
import json
from django.shortcuts import redirect
from .forms import ContactForm
# def feed(request):
#    if request.method == "POST":
#       cc = ContactForm(request.POST)
#       if cc.is_valid():
#           name = cc.cleaned_data['name']
#           mail=cc.cleaned_data['mail']
#           message=cc.cleaned_data['message']
#           cc.save()
#           return redirect('track') 
      
#    else:
#       cc = ContactForm(request.POST)
		
#    return render(request, 'contact.html',{"f":cc})

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
    if request.method == "POST":
      cc = ContactForm(request.POST)
      if cc.is_valid():
          name = cc.cleaned_data['name']
          mail=cc.cleaned_data['mail']
          message=cc.cleaned_data['message']
          cc.save()
          return redirect('track') 
      
    else:
      cc = ContactForm(request.POST)
    parms={
        "data":apiforindia(),
        "data2":apiforworld(),
        'f':cc
    }
    return render(request, 'main.html', parms)

def globalD(request):
    if request.method == "POST":
      cc = ContactForm(request.POST)
      if cc.is_valid():
          name = cc.cleaned_data['name']
          mail=cc.cleaned_data['mail']
          message=cc.cleaned_data['message']
          cc.save()
          return redirect('tracks') 
      
    else:
      cc = ContactForm(request.POST)
    parms={
        "data1":country(),
        "data":apiforindia(),
        "data2":apiforworld(),
        'f':cc
    }
    return render(request, 'global.html', parms)

