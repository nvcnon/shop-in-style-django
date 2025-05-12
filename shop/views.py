from django.contrib.auth import authenticate, login, logout 
from . import models 
from django.shortcuts import render, redirect 
from django.contrib import messages
# new
from django.contrib import humanize 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
# from .forms import SignUpForm

def homeView(request):
    all_product = models.Product.objects.all()
    return render(request, 'home.html', { 'products' : all_product} )

def aboutView(request):
    return render(request, 'about.html')

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)

        if user is not None :
            login(request, user)
            messages.success(request, ('you success logedin'))
            return redirect('homeView')
        else: 
            messages.success(request, ('we have a problem in login your info'))
            return redirect('loginView')
    else : 
        return render(request, 'login.html')
    
def logoutView(request):
    logout(request)
    messages.success(request, 'your success logedout')
    return redirect('homeView')

def productPageView(request, pk):
    product = models.Product.objects.get(id=pk)
    return render(request, 'productPage.html', {'product' : product})

def categoryView(request, cat):
    cat = cat.replace('-', ' ')
    try : 
        category = models.Category.objects.get(name = cat)
        products = models.Product.objects.filter(category = category)
        return render(request, 'category.html', { 'category' : category, 'products' : products})
    except:
        messages.success(request, 'not found category')
        return redirect('homeView')
    
# def signupView(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            # form.save()
            form.save(commit=True)
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username= username, password= password1)
            login(request, user)
            messages.success(request, ('your account succesfully created'))
            return redirect('homeView')
        else: 
            messages.success('we have problem in signup !')
            return redirect('signupView')
    else:
        return render(request, 'signup.html', {'form' : form})

# def signupView(request):
#     return render (request, 'signup.html', {}) 


def signupView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # some code
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('loginView')

        else:
            return redirect('homeView')
    else:
        return render(request, 'signup.html')