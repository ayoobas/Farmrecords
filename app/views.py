from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from .forms import FarminputForm, StaffRegisterForm
from .models import User
from .models import Farminputs



from .models import Farminputs

def home(request):
    return render(request,"index.html", locals())
    

#Display form records
def records(request):
    recordz = Farminputs.objects.all().order_by('-created_at')

    context = {
        'recordz':recordz, 
    }
    return render(request,"records.html", context)

# for login

def login_def(request):
    return render(request,"login.html", locals())

#Input farm records
def register(request):
    if request.method == 'POST':
        form = FarminputForm(request.POST)
        if form.is_valid():
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
        return redirect('login_def')

    # delete farm input
def farmrecords_delete(request, pk):
    item = Farminputs.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Record deleted Successfully.")
        return redirect('viewrecords')
    return render(request, "delete_farminput.html", locals())

#To edit records
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