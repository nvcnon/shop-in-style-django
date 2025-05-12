from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homeView, name='homeView'),
    path("about/", views.aboutView , name="aboutView"),
    path("login/", views.loginView , name="loginView"),
    path("logout/", views.logoutView , name="logoutView"),
    path("products/<int:pk>", views.productPageView , name="productPageView"),
    path("category/<str:cat>", views.categoryView , name="categoryView"),
    path("signup/", views.signupView , name="signupView"),
]
