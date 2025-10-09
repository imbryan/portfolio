from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from constance import config

class CustomAdminSite(admin.AdminSite):
    """
    https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#customizing-the-adminsite-class
    https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#overriding-the-default-admin-site
    """
    site_header = site_title = f'{getattr(config, 'BRAND')} Admin'
    index_title = 'Admin interface'

    def login(self, request, extra_context=None):
        return redirect(reverse('login'))
