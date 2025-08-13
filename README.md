# Running
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