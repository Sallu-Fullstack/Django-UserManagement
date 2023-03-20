from django.shortcuts import render, redirect
from django.http import HttpResponse
from gpt1.models import User
from django.contrib import sessions, messages
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
users = User.objects.all()
def home(request):
    return render(request, 'home.html')

def update_user_ids():
    users = User.objects.order_by('id')
    for i, user in enumerate(users, start=1):
        user.user_id = i
        user.save()


def create_form(request):
    if request.method == "POST":
        email = request.POST.get("inemail")
        username = request.POST.get("inusername")
        password = request.POST.get("inpassword1")
        password_confirm = request.POST.get("inpassword2")

        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'User with this username already exists')
        elif not password:
            messages.error(request, 'Enter the All the Fields!')
        elif password != password_confirm:
            messages.error(request, 'Password Dosen\'t Match.')
        else:
            user = User(email=email, username=username, password=password)
            user.save()
            messages.success(request, 'Account Created Successfully!')
            
            # create session for authenticated user
            if 'email' in request.session:
                del request.session['email']
                del request.session['username']
                del request.session['password']
            request.session['email'] = email
            request.session['username'] = username
            request.session['password']= password
            request.session.set_expiry(300) # set session timeout to 5 minutes (300 seconds)
            update_user_ids()
            return redirect("show_users")

    return render(request, "signup.html")




def show_users(request):
    update_user_ids()
    users = User.objects.order_by('id')
    if 'username' in request.session:
        return render(request, "users.html", {"users": users})
    else:
        messages.error(request, "You are not Logged In")
        return redirect('index')

def logout(request):
        if 'email' in request.session:
            del request.session['email']
            del request.session['username']
            del request.session['password']
        else:
            del request.session['username']
            del request.session['password']
        messages.error(request, "Logged Out Successfully, Login to view Users")
        return redirect('index')

def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        email = request.POST.get('inemail')
        username = request.POST.get('inusername')
        password = request.POST.get('inpassword1')
        password_confirm = request.POST.get("inpassword2")
        if email and username and password and password == password_confirm:
            user.email = email
            user.username = username
            user.password = password
            user.save()
            messages.success(request, 'User updated successfully!')
            update_user_ids()
            return redirect('show_users')
        else:
            messages.error(request, 'Please fill all the fields or Passwords don\'t match!')
    return render(request, 'edit_user.html', {"user" : user}) 

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    if user:
        user.delete()
        messages.success(request, 'User Deleted Successfully!')
        update_user_ids()
        return redirect('show_users')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('inusername')
        password = request.POST.get("inpassword")
        user_name = User.objects.filter(username=username).exists()
        user_password = User.objects.filter(password=password).exists()

        if not (user_name and user_password):
            messages.error(request, "Username and Password Doesn\'t exists, Sign Up")
        else:
            request.session['username']= username
            request.session['password']= password
            messages.success(request, f'Welcome {username}, You have Logged in Successfully')
            return redirect("show_users")

    return render(request, "index.html")

def search_username(request):
    if request.method == 'POST':
        username = request.POST.get("in_username")
        username = username.replace(" ", "")
        # users = User.objects.get()
        
        try:
            user = User.objects.get(username=username)
            messages.success(request, 'User Found Successfully!')
            return render(request, 'users.html', {"user": user})
        except ObjectDoesNotExist:
            messages.error(request, 'Username Doesn\'t exists')
            return redirect('show_users')

