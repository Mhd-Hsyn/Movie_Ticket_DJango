from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import Custom_UserCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Custom_UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print ("register successfully")
            return redirect('user:login')
    else:
        form = Custom_UserCreationForm()
    return render(request, 'register.html', {'form': form})



def _login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(username = username, password= password)
            
            if user is not None:
                login(request, user)
                return redirect('movie:dashboard')
            
            else : 
                pass
        else:
            print(ValueError)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})