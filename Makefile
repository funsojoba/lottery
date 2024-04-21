COMPOSE=docker compose
SERVICE=web


up:
	$(COMPOSE) up

down:
	$(COMPOSE) down

build:
	$(COMPOSE) build

shell:
	$(COMPOSE) run --rm $(SERVICE) python manage.py shell


migrations:
	$(COMPOSE) run --rm $(SERVICE) python manage.py makemigrations

showmigrations:
	$(COMPOSE) run --rm $(SERVICE) python manage.py showmigrations

migrate:
	$(COMPOSE) run --rm $(SERVICE) python manage.py migrate


superuser:
	$(COMPOSE) run --rm $(SERVICE) python manage.py createsuperuser