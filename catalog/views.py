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
import random



# Create your views here.
def home(request):

    a=random.randint(4,1003)
    b=a+1
    poem_list=poem.objects.all()[a:b]
    context={
        'poem_list':poem_list
    }

    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

def poem_detail(request, pk):
    post = poem.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})