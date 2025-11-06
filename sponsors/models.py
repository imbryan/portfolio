from django.db import models


class Sponsorship(models.Model):
    id = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=50)
    platform_message_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)
    is_message_public = models.BooleanField(default=True)
    start_date = models.DateTimeField()

    raw_payload = models.JSONField(null=True, blank=True)
    expiration_date = models.DateTimeField()
    processed = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['platform', 'platform_message_id'], name='unique_platform_platform_message_id'),
        ]
