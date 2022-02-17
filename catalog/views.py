from encodings import utf_8, utf_8_sig
import imp
import os
import json 
from importlib.resources import contents
from sys import modules
from tokenize import Ignore
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context  
from catalog.models import poem
from django.conf import settings




fp = open("poem.json", "r", encoding="utf-8")
rawdata = fp.read()
fp.close()

data = json.loads(rawdata)
print("詩名：", data[0]['title'])
print("作者：", data[0]['author'])
print("內容：", "".join(data[0]['paragraphs']))

# Create your views here.
def home(request):
    
    context={
        'poems':data
    }

    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})