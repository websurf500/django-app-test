from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponse("<h1>Home Page</h1>")
def about(request):
    return HttpResponse("<h1>About Us Page</h1>")
from django.contrib.auth.models import User 
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        userobj = User.objects.create(username = username,password = password)
        userobj.save()
        return HttpResponseRedirect('/myapp2/login')

    return render(request,'register.html')

from django.contrib.auth import authenticate

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Username:", username)
        print("Password:", password)
        user = authenticate(username=username, password=password)
        if user is not None:
            # User authenticated successfully
            print("Authenticated user:", user)
            # Redirect the user to some page or do something else
        else:
            # Authentication failed
            print("Invalid credentials")
             # Handle invalid credentials
    return render(request,'login.html')


