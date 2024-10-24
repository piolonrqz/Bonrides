from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm # import from forms.py
from django.contrib.auth import authenticate, login as auth_login # auth
from django.contrib.auth import logout as auth_logout # logout
from django.contrib import messages

# Create your views here.
def homepage(request):
    context = {}
    return render(request, 'bonrides_rental/homepage.html', context)

def about(request):
    context = {}
    return render(request, 'bonrides_rental/about.html', context)

def vehicles(request):
    context = {}
    return render(request, 'bonrides_rental/vehicles.html', context)

def booking(request):
    context = {}
    return render(request, 'bonrides_rental/booking.html', context)

def contacts(request):
    context = {}
    return render(request, 'bonrides_rental/contacts.html', context)

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'bonrides_rental/login.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'bonrides_rental/register.html', context)

def user_logout(request):
    auth_logout(request)
    return redirect('login')