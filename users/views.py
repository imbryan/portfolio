from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('home:index'))
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(reverse('home:index'))
        else:
            return render(request, 'users/login.html', {'form': form})
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect(getattr(settings, 'LOGOUT_REDIRECT_URL', reverse('home:index')))
