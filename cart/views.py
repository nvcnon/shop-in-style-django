from django.shortcuts import render, get_object_or_404
from .cart import Cart 
from shop.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary_view(request):
    return render(request, 'cart_summary.html', {})

def cart_add_view(request):
    cart = Cart(request)

    if request.POST.get('action')  == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

    response = JsonResponse({'Product name' : product.name})
    return response

def cart_delete_view(request):
    pass 

def cart_update_view(request):
    pass 