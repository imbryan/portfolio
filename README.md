# Portfolio
[![Tests](https://github.com/imbryan/portfolio/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/imbryan/portfolio/actions/workflows/test.yml)

Personal website that includes a portfolio and a blog. Made with [Django](https://github.com/django/django).

## Setup
### Environment variables
#### Always required
- ``DEBUG`` (True/False)
- ``SECRET_KEY``
- ``ALLOWED_HOSTS`` (comma-separated values)

#### For development
- ``DATABASE_PATH`` (e.g. ``path/to/portfolio/db/db.sqlite3``)

#### [OpenID Connect](https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html)
- ``OIDC_RP_CLIENT_ID``
- ``OIDC_RP_CLIENT_SECRET``
- ``OIDC_RP_SIGN_ALGO``
- ``OIDC_OP_JWKS_ENDPOINT``
- ``OIDC_OP_AUTHORIZATION_ENDPOINT``
- ``OIDC_OP_TOKEN_ENDPOINT``
- ``OIDC_OP_USER_ENDPOINT``

#### Cloudflare Turnstile
- ``TURNSTILE_SITE_KEY``
- ``TURNSTILE_SECRET_KEY``

#### Django-Axes
- ``AXES_ENABLED``
- ``AXES_IPWARE_PROXY_COUNT``
- ``AXES_FAILURE_LIMIT``

## File structure
### Python imports
1. Third-party libraries
2. Python standard library
3. Custom modules

### Django project apps
- ``api``: REST API.
- ``home``: index page, project portfolio, and blog features.
- ``users``: authentication.

### Other directories
- ``assets``: Webpack source (pre-bundle).
- ``core``: Django project utils.
- ``portfolio``: Django project settings.
- ``static``: Django static files (pre-collection).
- ``templates``: Django project templates.

## Development
### Generating the requirements lock
- ``pip-compile pyproject.toml --output-file requirements.txt``
- ``pip-compile pyproject.toml --output-file requirements.dev.txt --extra dev``

### Making changes to models
1. Make changes in ``models.py``
2. Register as needed in ``admin.py``
3. Make sure ``DATABASE_PATH`` is set in ``.env`` (cross-reference ``docker-compose*.yml``)
4. In a venv, run ``python manage.py makemigrations``

### Linting
- ``ruff check``

### Running in Docker
``docker compose -f docker-compose.yml up -d --build``


## Production
### Running in Docker
``docker compose -f docker-compose.prod.yml up -d --build``
