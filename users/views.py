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
            remoteip = request.headers.get('CF-Connecting-IP') or \
                request.headers.get('X-Forwarded-For') or \
                request.META.get('REMOTE_ADDR')
            
            if not token or not validate_turnstile(token, settings.TURNSTILE_SECRET_KEY, remoteip)['success']:
                form.add_error(None, "Security challenge failed. Please try again.")

        # Validate form/credentials
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(reverse('home:index'))
        else:
            if request.headers.get('HX-Request') == 'true':
                response = render(request, 'users/partials/login_form.html', {'form': form})
                response.status_code = 401
                return response
            return render(request, 'users/login.html', {'form': form})

    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect(getattr(settings, 'LOGOUT_REDIRECT_URL', reverse('home:index')))
