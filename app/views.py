from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from .forms import FarminputForm



from .models import Farminputs

def home(request):
    return render(request,"index.html", locals())
     #return render(request,"records.html", locals())

def records(request):
    return render(request,"records.html", locals())

def login_def(request):
    return render(request,"login.html", locals())


def register(request):
    if request.method == 'POST':
        form = FarminputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewrecords')
      
    else:
        form = FarminputForm()
        
    context = {
        "form": form
    }

    
    return render(request, "inputregister.html", context)