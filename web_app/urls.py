from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('checkout/', views.checkout, name="checkout"),
    path('Login/', views.Login, name='Login'),
    path('Register/', views.Register, name='Register'),
    path('clientAreaLogin/', views.clientAreaLogin, name='clientAreaLogin'),
]