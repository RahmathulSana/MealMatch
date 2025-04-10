from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.http import HttpResponse


def home(request):
    return render(request,'users/home.html')
def contact(request):
    return render(request,'users/contact.html')
def about(request):
    return render(request,'users/about.html')
def home(request):
    return render(request,'users/home.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create user but don't save yet
            user.save()  # Save user in database
            return redirect('users:login')  # Correct way to redirect
    
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

def create(request):
    return HttpResponse("User successfully created!")  # Confirm successful creation
def is_seller(user):
    return user.role == 'seller'

def is_buyer(user):
    return user.role == 'buyer'




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.role == 'seller':
                    return redirect('food:welcome')  # Redirect to seller page
                else:
                    return redirect('order:browse_food')  # Redirect to buyer page
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)  # Logs out the user
    request.session.flush()  # Clears all session data
    return redirect('users:login')  # Redirect to login page
