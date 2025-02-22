from django.shortcuts import render
import django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello worl, my first django project")

def new(request):
    data=datetime.datetime.now()
    h=int(date.strftime("%H"))

    if h<12:
        msg = "hello everyone ...! good morning tag"
    elif h<16:
        msg = "hello everyone...! good afternoon"
    elif h<21:
        msg = "hello everyone...! good evening"
    else:
        msg = "hello everyone...! time to sleep good night"

    return render(request,"app/home.html")