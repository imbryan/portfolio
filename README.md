# Running
## Environment
- Always set: ``DEBUG``, ``SECRET_KEY``, ``ALLOWED_HOSTS``
- Set for development: ``DATABASE_PATH``, ``FORWARDED_ALLOW_IPS``
- Set for OIDC SSO: ``OIDC_RP_CLIENT_ID``, ``OIDC_RP_CLIENT_SECRET``, ``OIDC_RP_SIGN_ALGO``, ``OIDC_OP_JWKS_ENDPOINT``, ``OIDC_OP_AUTHORIZATION_ENDPOINT``, ``OIDC_OP_TOKEN_ENDPOINT``, ``OIDC_OP_USER_ENDPOINT`` (see [docs](https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html))
- Set for Axes: ``AXES_IPWARE_PROXY_COUNT``, ``AXES_FAILURE_LIMIT``

## Development
``docker compose -f docker-compose.yml up -d --build``

## Production
``docker compose -f docker-compose.prod.yml up -d --build``

# Workflow
## Models
1. Make changes in ``models.py``
2. Register as needed in ``admin.py``
3. Make sure ``DATABASE_PATH`` is set in ``.env`` (cross-reference ``docker-compose*.yml``)
4. In a venv, run ``python manage.py makemigrations``