from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from constance import config

class CustomAdminSite(admin.AdminSite):
    """
    https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#customizing-the-adminsite-class
    https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#overriding-the-default-admin-site
    """
    index_title = 'Admin interface'

    # Defer config database access to fix RuntimeWarning
    @property
    def site_title(self):
        return f'{getattr(config, 'BRAND')} Admin'
    
    @property
    def site_header(self):
        return self.site_title

    def login(self, request, extra_context=None):
        return redirect(reverse('login'))
