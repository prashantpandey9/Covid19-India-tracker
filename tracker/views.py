from django.shortcuts import render
import requests
import json

def api():
    api="https://api.covid19india.org/data.json"

    s=(requests.get(api)).text

    data=json.loads(s)
    b=1
    return data

# Create your views here.
def Track(request):
    parms={
        "data":api(),
    }
    return render(request, 'main.html', parms)