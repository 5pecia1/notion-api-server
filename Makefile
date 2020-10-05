PYTHON := python3
PIP := pip3

venv:
	@echo "virtualenv can be installed by: pip3 install virtualenv"
	rm -rf venv
	virtualenv -p $(PYTHON) venv
	source venv/bin/activate;\
		$(PIP) install notion-py;\
		$(PYTHON) --version;\
		$(PIP) --version;\
		$(PIP) install -r requirements.txt;
	@echo "Active the virtual env: source venv/bin/activate"
	@echo "Deactive when done: deactivate"

docker:
	@docker build -f ./Dockerfile -t notion-api-server:latest .

docker-up:
	@docker-compose up -d

docker-down:
	@docker-compose down -v
