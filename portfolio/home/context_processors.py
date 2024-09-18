from django.conf import settings

def global_settings(request):
    return {
        'ADSENSE_CLIENT': getattr(settings, 'ADSENSE_CLIENT', None)
    }
