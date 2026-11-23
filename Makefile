APP = reestapi

test: 
	@echo "Running linting..."
	@flake8 . --exclude .venv   

compose: test
	@echo "Running docker compose..."
	docker compose up --build