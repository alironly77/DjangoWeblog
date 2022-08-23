from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.sign_up, name='signup'),
    path('Login/', views.login_page, name='login'),
    path('Logout/', views.logout_page, name='logout'),
]
