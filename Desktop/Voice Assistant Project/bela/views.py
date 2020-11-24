from django.shortcuts import render
import requests
import sys
from subprocess import PIPE
from subprocess import call

def button(request):
    return render(request,'home.html')

def mic(request):
    while True:
        
        out=call([sys.executable,'C:\\Bela\\bela.py'],shell=True,stdout=PIPE)
        print(out)
        return render(request,'home.html')

def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})

def external(request):
    while True:
        inp=request.POST.get('param')
        out=call([sys.executable,'C:\\Bela\\bela.py',inp],shell=True,stdout=PIPE)
        print(out)
        inp=""
        sys.argv[1]=""
        return render(request,'home.html')

    
