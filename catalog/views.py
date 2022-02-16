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



p = open(os.path.join(settings.BASE_DIR, 'poem.json'),encoding='UTF-8')

# Create your views here.
def home(request):
    
    context={
        'poems':p
    }

    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})