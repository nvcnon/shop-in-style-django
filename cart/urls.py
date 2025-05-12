from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.cart_summary_view , name="cart_summary_view"),
    path("add/", views.cart_add_view , name="cart_add_view"),
    path("delete/", views.cart_delete_view , name="cart_delete_view"),
    path("update/", views.cart_update_view , name="cart_update_view"),
]
