from django.conf import settings

def global_settings(request):
    return {
        'OIDC_CONFIGURED': getattr(settings, 'OIDC_CONFIGURED', False),
        'OIDC_OP_DISPLAY_NAME': getattr(settings, 'OIDC_OP_DISPLAY_NAME', None) or 'SSO',
        'TURNSTILE_SITE_KEY': getattr(settings, 'TURNSTILE_SITE_KEY', None),
    }