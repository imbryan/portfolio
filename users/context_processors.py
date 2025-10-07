from django.conf import settings

def global_settings(request):
    return {
        'oidc_configured': getattr(settings, 'OIDC_CONFIGURED', False),
        'oidc_op_display_name': getattr(settings, 'OIDC_OP_DISPLAY_NAME', None) or 'SSO',
    }