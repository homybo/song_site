from encodings import utf_8, utf_8_sig
import imp
import os
import json 
from importlib.resources import contents
from sys import modules
from tokenize import Ignore
from turtle import title
from django.shortcuts import render
from catalog.models import Poem
from django.conf import settings
import random
from django.core.paginator import Paginator



# Create your views here.
def home(request):
    poem=Poem.objects.all()
    target = random.choice(poem)
    return render(request,'blog/home.html',locals())

def about(request):
    return render(request,'blog/about.html',locals())

def showall(request):
    poem = Poem.objects.all()
    limit=10
    page=request.GET.get('page',1)
    paginator = Paginator(poem,limit)
    Poem_All=paginator.page(page)

    return render(request, "blog/showall.html", locals())

def show(request, id):
    target = Poem.objects.get(id=id)
    return render(request, "blog/show.html", locals())