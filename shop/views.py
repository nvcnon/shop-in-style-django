from . import models 
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib import humanize 

def homeView(request):
    all_product = models.Product.objects.all()
    return render(request, 'home.html', { 'products' : all_product} )

def aboutView(request):
    return render(request, 'about.html')
    

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
    

