from django.shortcuts import render
from django.shortcuts import render, redirect
from users.forms import UserRegister, LoginForm, ProfileUpdate
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from event.models import Event
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.

def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("home")
    context = {
        "form": form,
    }

    return render(request, "register.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("home")
    
    context = {
        "form": form,
    }
    return render(request, "login.html", context)


@login_required 
def get_user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    
    event_items: list[Event] = list(Event.objects.all())
    
    context= {
       "user":{
        "id": user.id,
        "first_name": user.first_name,
        "last_name":user.last_name,
        "email":user.email,},

        "event_items": event_items,
        

       }

    
    return render(request, "profile-user.html", context)

def get_organizer_profile(request, user_id):
    user = User.objects.get(id=user_id)
    
    event_items: list[Event] = list(Event.objects.all())
    
    context= {
       "user":{
        "id": user.id,
        "first_name": user.first_name,
        "last_name":user.last_name,
        "email":user.email,},

        "event_items": event_items,
        

       }

    
    return render(request, "profile-organizer.html", context)



def update_profile(request, user_id):
    user = User.objects.get(id=user_id)
    form = ProfileUpdate(instance=user)
    if request.method == "POST":
        form = ProfileUpdate(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile_user", user_id)
    context = {
        "user": user,
        "form": form,
    }
    return render(request, "update-profile.html", context)

