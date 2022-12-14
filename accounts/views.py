from django.shortcuts import render, redirect
from .forms import SignupForm , LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
            cd['username'], cd['email'], cd['password'],)
            user.save()
            messages.success(request, 'User Register Successfully', 'success')
            return redirect('articles_app:Home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def UserLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(
                    request, 'User logged Successfully', 'success')
                return redirect('articles_app:Home')
            else:
                messages.error(
                    request, 'username or password is wrong', 'danger')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def UserLogout(request):
    logout(request)
    return redirect('articles_app:Home')
