COMPOSE=docker compose


up:
	$(COMPOSE) up

down:
	$(COMPOSE) down

build:
	$(COMPOSE) build