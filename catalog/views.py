from importlib.resources import contents
from unicodedata import name
from django.shortcuts import render
from catalog.models import Poem
from django.core.paginator import Paginator
import random



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

def search(request):
    if request.method=="POST":  
        search_title= request.POST.get('search_title')
        search_author= request.POST.get('search_author')
        results_title=Poem.objects.filter(title__contains=search_title)
        results_author=Poem.objects.filter(author__contains=search_author)
        return render(request,"blog/results.html",locals())