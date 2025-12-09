from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from .forms import FarminputForm, StaffRegisterForm, FarminputtwoForm
from .models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 
from django.utils.dateparse import parse_date
from datetime import datetime
from django.utils import timezone
from .models import Farminputs, Farminputtwo, RequestFarmrecordupdates

def home(request):
    return render(request,"index.html", locals())
    

#Display farm records
@login_required(login_url = 'user_login')
def records(request):
    recordz = Farminputs.objects.all().order_by('-created_at')
    #For the search from to date
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')
    if from_date:
        recordz  = recordz .filter(created_at__date__gte=parse_date(from_date))
    if to_date:
        recordz  = recordz .filter(created_at__date__lte=parse_date(to_date))

    paginator = Paginator(recordz, 4)
    page_number = request.GET.get('page')
    venues = paginator.get_page(page_number)

    context = {
        'venues': venues,
        'from_date': from_date,
        'to_date': to_date
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
@login_required(login_url='user_login')
def register(request):
    if request.method == 'POST':
        form = FarminputForm(request.POST)
        formtwo = FarminputtwoForm(request.POST)

        if form.is_valid() and formtwo.is_valid():
            # Save Farminputs first
            farminput = form.save(commit=False)
            farminput.user = request.user
            farminput.save()

            # Link second form
            formtwo_instance = formtwo.save(commit=False)
            formtwo_instance.FI = farminput
            formtwo_instance.save()

            messages.success(request, "✅ Farm record added successfully!")
            return redirect('viewrecords')
    else:
        form = FarminputForm()
        formtwo = FarminputtwoForm()

    context = {'form': form, 'formtwo': formtwo}
    return render(request, 'inputregister.html', context)


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
def farmrecords_edit(request, pk):
    # Get the Farminputs record
    item = Farminputs.objects.get(id=pk)
    # Try to get the related Farminputtwo (if it exists)
    try:
        item_two = Farminputtwo.objects.get(FI=item)
    except Farminputtwo.DoesNotExist:
        item_two = None  # if it doesn't exist yet
    
    if request.method == 'POST':
        form = FarminputForm(request.POST, instance=item)
        formtwo = FarminputtwoForm(request.POST, instance=item_two)

        if form.is_valid() and formtwo.is_valid():
            # Save Farminputs first
            updated_item = form.save()
            # Save or create Farminputtwo
            updated_item_two = formtwo.save(commit=False)
            updated_item_two.FI = updated_item  # Link to Farminputs
            updated_item_two.save()

            #update RequestFarmrecordupdate table
            updaterectified(item.id)

            messages.success(request, "✅ Record updated successfully.")
            return redirect('viewrecords')

    else:
        form = FarminputForm(instance=item)
        formtwo = FarminputtwoForm(instance=item_two)

    context = {
        'form': form,
        'formtwo': formtwo,
        'itemid':item.id
    }

    return render(request, 'edit_farminginput.html', context)

def updaterectified(record_id):
    # Get the Farminputs object
    item = Farminputs.objects.get(id=record_id)
    # Update all requests linked to this item
    RequestFarmrecordupdates.objects.filter(record_id=item.id).update(rectified=True)

##View staff profile
@login_required(login_url = 'user_login')
def staff_profile(request):
    return render(request, 'profile.html')

## List of staff 
@login_required(login_url = 'user_login')
def staff_list(request):
    return render(request, 'staff_list.html')

#Display Update request List
@login_required(login_url = 'user_login')
def updatefarmrecordlist(request):

    item = RequestFarmrecordupdates.objects.all().order_by('-created_at')
    
    return render(request , 'updaterequest_list.html', {'item':item})


#Request from Admin to update farm records
def Requestupdate(request, pk):
    item = Farminputs.objects.get(id=pk)

    if request.method == "POST":
        description = request.POST.get("reqdescription")

        if description is None or description.strip() == "":
            messages.warning(request, "Please enter some value.")
            return redirect(request.path)   # Reload page

        if not request.user.is_authenticated:
            messages.warning(request, "You must be logged in to submit a request.")
            return redirect("login")

        # Save request
        RequestFarmrecordupdates.objects.create(
            user=request.user,
            record_id=pk,
            request=description,
            rectified=False
        )

        messages.success(request, "Request was saved successfully.")
        return redirect("viewrecords")

    return render(request, "request_updateinputrecords.html", {"item": item})



 # delete farm input
@login_required(login_url = 'user_login')
def Requestfarmrecorddelete(request, pk):
    item = RequestFarmrecordupdates.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Record deleted Successfully.")
        return redirect('updatefarmrecordlist')
    return render(request, "delete_requestupdate.html", locals())


#update staff_profile
@login_required(login_url = 'user_login') 
def staff_profile_update(request):

    context = {

    }

    return render(request, 'profile_update.html', context)











#for good day , good afternoon
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