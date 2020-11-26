from django.shortcuts import render
import requests
import json
from django.shortcuts import redirect
from .forms import ContactForm
from bs4 import BeautifulSoup
from datetime import datetime
now = datetime.now()

def apiforindia():
    api="https://api.covid19india.org/data.json"

    s=(requests.get(api)).text

    data=json.loads(s)
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

def district():
    api="https://api.covid19india.org/v2/state_district_wise.json"

    s=(requests.get(api)).text

    data=json.loads(s)
    return data

def news():
    url="https://news.google.com/topics/CAAqBwgKMMqAmAsw9KmvAw?hl=en-IN&gl=IN&ceid=IN%3Aen" #google news URL for scraping it.
    q=requests.get(url)
    soup=BeautifulSoup(q.text,"html.parser")
    news_headline=soup.find_all('h3',class_="ipQwMb ekueJc RD0gLb") # News Headline
    images = soup.findAll('img',class_="tvs3Id QwxBBf") #Image links related to News-headline
    link = soup.findAll('a',class_="VDXfz") # News-Headline deatail link
    news_headline_list=[n.text for n in news_headline]
    image_link=[j['src'] for j in images]
    headline_link=["https://news.google.com/"+str(j['href']) for j in link]

    serial=1
    value=[]
    for j in range(20):
        value.append({"serial":serial,"date":now.strftime("%d %b"),"Headline":news_headline_list[j],"image_link":image_link[j],"headline_link":headline_link[j]})
        serial+=1

    # with open("google-news"+str(now.strftime(" %d%b"))+".json", 'w') as file:
    #     json.dump(value, file)
    return value

# Views START FROM HERE
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
        'f':cc,

    }
    return render(request, 'global.html', parms)


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
        "dist":district(),
        'f':cc
    }
    return render(request, 'main.html', parms)

def News(request):
    parms={
        "news":news(),
        "now":now
    }
    return render(request, 'news.html', parms)

def DistrictWise(request):
    parms={

        "data1":district(),
    }
    return render(request,'districtwise.html',parms)