from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import OIDCProfile

User = get_user_model()

class OIDCProfileInline(admin.StackedInline):
    model = OIDCProfile
    can_delete = False
    verbose_name_plural = "OIDC Profile"


class CustomUserAdmin(UserAdmin):
    inlines = (OIDCProfileInline,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)