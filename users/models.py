from django.contrib.auth.models import User
from django.db import models

class OIDCProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='oidc_profile')
    sub = models.CharField(max_length=255)
    iss = models.TextField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['iss', 'sub'], name='unique_iss_sub'),
        ]
        app_label = 'users'
        db_table = 'users_oidcprofile'

    def __str__(self):
        return f"{self.user.username} ({self.sub})"
