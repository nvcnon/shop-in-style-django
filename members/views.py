from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)

        if user is not None :
            login(request, user)
            messages.success(request, ('شما با موفقیت وارد شدید'))
            return redirect('homeView')
        else: 
            messages.success(request, ('پسورد شما اشتباه است'))
            return redirect('loginView')
    else : 
        return render(request, 'login.html')
    

def logoutView(request):
    logout(request)
    messages.success(request, 'your success logedout')
    return redirect('homeView')

def signupView(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('loginView')
    else:
        return render(request, 'signup.html', {'form':form})
        


# def registerView(request):
#     form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('loginView')
#     else:
#         return render(request, 'authentication/register.html', {'form':form})
