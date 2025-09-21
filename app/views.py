from django.shortcuts import render, redirect
from django.views import View

def home(request):
    #return render(request,"index.html", locals())
     return render(request,"records.html", locals())

def records(request):
    return render(request,"records.html", locals())