from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.sign_up, name='signup'),
    path('Login/', views.UserLogin, name='login'),
    path('Logout/', views.UserLogout, name='logout'),
]
