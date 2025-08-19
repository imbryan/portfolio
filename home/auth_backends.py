from django.contrib.auth import get_user_model
from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from .models import OIDCProfile

User = get_user_model()

class CustomOIDCAuthenticationBackend(OIDCAuthenticationBackend):
    """
    https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html#connecting-oidc-user-identities-to-django-users
    """
    def filter_users_by_claims(self, claims):
        # https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims
        sub = claims.get('sub')
        email = claims.get('email')

        if sub:
            try:
                profile = OIDCProfile.objects.get(sub=sub)
                return [profile.user]
            except OIDCProfile.DoesNotExist:
                pass
        if email:
            try:
                user = User.objects.get(email=email)
                return [user]
            except User.DoesNotExist:
                pass
        return User.objects.none()
    
    def create_user(self, claims):
        user = super().create_user(claims)
        preferred_username = claims.get('preferred_username')
        if preferred_username and not User.objects.filter(username=preferred_username).exists():
            user.username = preferred_username
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()

        OIDCProfile.objects.create(
            user=user,
            sub=claims.get('sub'),
        )
        return user
    
    def update_user(self, user, claims):
        profile, created = OIDCProfile.objects.get_or_create(user=user)
        if created:
            profile.sub = claims.get('sub')
            profile.save()
        return user

