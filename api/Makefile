COMPOSE_FILE=docker-compose.dev.yml
ENV_FILE=.env

start-db:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up -d db

stop-db:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) stop db

clean-db:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) down -v

logs-db:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) logs -f db

status:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) ps

# Starts DB and runs Django dev server (sync)
runserver: start-db
	uv run python manage.py runserver

# Starts DB and runs ASGI GraphQL/Django server with uvicorn (async)
start: start-db
	uv run uvicorn config.asgi:application --reload --host 0.0.0.0 --port 8000

# usage: make makemigrations app=[app_name]
makemigrations:
	uv run python manage.py makemigrations $(app)

# usage: make migrate
migrate:
	uv run python manage.py migrate

# usage: make reset-db
reset-db: clean-db start-db migrate

# usage: make load-data file=path/to/users.json
load-data:
	uv run python manage.py loaddata $(file)

# usage: make flush
# WARNING: This will delete all data in the database!
flush:
	uv run python manage.py flush --no-input
	
# usage: make dumpdata
# Dumps all data to data.json
# WARNING: This will overwrite data.json!
dumpdata:
	uv run python manage.py dumpdata > data.json