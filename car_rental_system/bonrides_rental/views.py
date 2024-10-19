from django.shortcuts import render

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

def login(request):
    context = {}
    return render(request, 'bonrides_rental/login.html', context)

def register(request):
    context = {}
    return render(request, 'bonrides_rental/register.html', context)
