from django.apps import AppConfig


# overrides mcfatter-cafe.cafe.apps.CafeConfig
class CafeConfig(AppConfig):
    name = 'mcfatter-cafe.cafe'