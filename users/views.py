from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

from core.utils.turnstile_utils import validate_turnstile

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('home:index'))
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        # Validate Turnstile token
        if settings.TURNSTILE_CONFIGURED:
            token = request.POST.get('cf-turnstile-response')
            if not token:
                form.add_error(None, "Security challenge failed. Please refresh and try again.")
                return render(request, 'users/login.html', {'form': form})
            remoteip = request.headers.get('CF-Connecting-IP') or \
                request.headers.get('X-Forwarded-For') or \
                request.META.get('REMOTE_ADDR')
            cf_validation = validate_turnstile(token, settings.TURNSTILE_SECRET_KEY, remoteip)
            if not cf_validation['success']:
                form.add_error(None, "Security challenge failed. Please refresh and try again.")
                return render(request, 'users/login.html', {'form': form})
        # Validate credentials
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
