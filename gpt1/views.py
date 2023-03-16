from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'home.html')

def create_form(request):
    if request.method == "POST":
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
    return render(request, "home.html", {"users": users}) 


