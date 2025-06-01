from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homeView, name='homeView'),
    path("about/", views.aboutView , name="aboutView"),
    path("products/<int:pk>", views.productPageView , name="productPageView"),
    path("category/<str:cat>", views.categoryView , name="categoryView"),
]
