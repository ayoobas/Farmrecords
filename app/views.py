from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from .forms import FarminputForm, StaffRegisterForm
from .models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 
from datetime import datetime
from django.utils import timezone
from .models import Farminputs



from .models import Farminputs

def home(request):
    return render(request,"index.html", locals())
    

#Display farm records
@login_required(login_url = 'user_login')
def records(request):
    recordz = Farminputs.objects.all().order_by('-created_at')

  
    page_list = Paginator(Farminputs.objects.all().order_by('-created_at'), 3)
    page = request.GET.get('page')
    venues = page_list.get_page(page)

    context = {
        'recordz':recordz, 
        'venues':venues
    }
    return render(request,"records.html", context)

# for login
def login_def(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request, user)
            #messages.success(request, ("You have been logged in!"))
            return redirect('viewrecords')
        else:
            messages.warning(request, ("incorrect username or password!"))
            return redirect('user_login')
        
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You  logged out"))
    return redirect('user_login')

#Input farm records
@login_required(login_url = 'user_login')
def register(request):
    if request.method == 'POST':
        form = FarminputForm(request.POST)
        if form.is_valid():
            farminput = form.save(commit=False)  
            farminput.user = request.user 
            form.save()
            messages.success(request, "Records Submitted Successfully.")
            return redirect('viewrecords')
      
    else:
        form = FarminputForm()
        
    context = {
        "form": form
    } 
    return render(request, "inputregister.html", context)


class StaffRegistration(View):
    def get(self, request):
        return render(request, 'staffregistration.html', locals())
    def post(self, request):
        # Handle the registration logic on POST requests
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

           # Validate the form data
        if not username or not email or not password or not cpassword:
            messages.warning(request, "All fields are required.")
            return render(request, 'staffregistration.html', locals())
        
        if password != cpassword:
            messages.warning(request, "Passwords do not match.")
            return render(request, 'staffregistration.html', locals())
          # Check if a user with the same username or email already exists

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already taken.")
            return render(request, 'staffregistration.html', locals())
        
        # Check if a user with the same username or email already exists
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already taken.")
            return render(request, 'staffregistration.html', locals())
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Congratulations! Profile saved successfully.")
        return redirect('user_login')

 # delete farm input
@login_required(login_url = 'user_login')
def farmrecords_delete(request, pk):
    item = Farminputs.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Record deleted Successfully.")
        return redirect('viewrecords')
    return render(request, "delete_farminput.html", locals())

#To edit records
@login_required(login_url = 'user_login')
def farmrecords_edit(request,pk):
    item = Farminputs.objects.get(id = pk)
    if request.method == 'POST':
        form = FarminputForm(request.POST, instance= item)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated Successfully.")
            return redirect('viewrecords')
    else:
        form = FarminputForm(instance = item)

    context = {
        'form':form,

    }
    return render(request, 'edit_farminginput.html', context)


@login_required(login_url='user_login')
def greeting_context(request):
    if not request.user.is_authenticated:
        return {}
    current_hour = timezone.now().hour

    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    context = {
        'greeting': greeting,
    }
    print("check", greeting)
    #return redirect('viewrecords')
    return render(request, 'base.html', context)