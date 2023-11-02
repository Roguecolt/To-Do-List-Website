from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import TaskForm
from myapp.models import Task


# Create your views here.
def index(request):
  
  return render(request, 'index.html')

def registration(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']

    if password == confirmpassword:
      
      if User.objects.filter(username=username).exists():
         messages.info(request, 'Username already in use')
         return redirect('/register')
      elif User.objects.filter(email=email).exists():
         messages.info(request, 'Email already in use')
         return redirect('/register')
      else:
          user = User.objects.create_user(username=username,email=email,password=password)
          user.save();
          return redirect('login')
    else:
       messages.info(request, 'Password not same')
  else:
    return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        remember_me = request.POST.get('remember-me')  # Check if "Remember Me" is selected

        user = auth.authenticate( username=username, email=email, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)

                if not remember_me:
                    # If "Remember Me" is not selected, set the session expiration to the default
                    request.session.set_expiry(86400)
                return redirect('/todoapp')
            else:
                messages.info(request, 'Account is not active')
        else:
            messages.info(request, 'Credentials invalid')
    return render(request, 'login.html')


def logout(request):
   auth.logout(request)
   return redirect('/')





def dashboard(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print(request.POST)  # Add this line to print the form data
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)  # Add this line to print form errors
    else:
        form = TaskForm()
    return render(request, 'dashboard.html', {'form': form})


def task_detail(request):
    tasks = Task.objects.all()
    return render(request, 'task-detail.html', {'tasks': tasks})

def todo_list(request):
    return render(request, 'todoapp.html')

def post(request, user):
   return render(request, 'todoapp.html', {user : 'user'})
