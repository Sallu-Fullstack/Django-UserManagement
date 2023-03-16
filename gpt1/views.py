from django.shortcuts import render, redirect
from django.http import HttpResponse
from gpt1.models import User
from django.contrib import sessions
# Create your views here.
users = User.objects.all()
def home(request):
    return render(request, 'home.html')

def create_form(request):
    if request.method == "POST":
        if "email" in session["email"]:
            request.session["email"] = email
            request.session["username"] = username
            request.session["password"] = password
            return render(request, "index.html", email, username, password)
        else:
            email = request.POST.get("inemail")
            username = request.POST.get("inusername")
            password = request.POST.get("inpassword1")
            password_confirm = request.POST.get("inpassword2")
        user = User(email=email, username=username, password=password)
        user.save()
        return render(request, "index.html")
    

    return render(request, "index.html")


def show_users(request):
    users = User.objects.all()
    print(users)
    return render(request, "home.html", {"users": users})

def logout(request):
    email = request.session.get('email')
    username = request.session.get('username')
    password = request.session.get('password')

    return redirect('home')
