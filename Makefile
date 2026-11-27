APP = reestapi

teste:
	@echo "Running tests..."
	@pytest -v --disable-warnings --maxfail=1

test: 
	@echo "Running linting..."
	@flake8 . --exclude .venv   


compose: test
	@echo "Running docker compose..."
	docker compose up --build