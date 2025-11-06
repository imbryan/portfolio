from django.contrib import admin

from .models import Sponsorship


class SponsorshipAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Data', {'fields': ['platform', 'platform_message_id', 'amount', 'currency', 'name', 'message', 'is_message_public', 'start_date']} ),
        ('Metadata', {'fields': ['raw_payload', 'expiration_date', 'processed', 'hidden']} ),
    ]

    readonly_fields = ['raw_payload', 'processed']


admin.site.register(Sponsorship, SponsorshipAdmin)
