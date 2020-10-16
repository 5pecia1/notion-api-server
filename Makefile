DOCKER_VERSION := latest
DOCKER_IMAGE := 5pecia1/notion-api-server

PYTHON := python3
PIP := pip3


init-venv:
	echo "virtualenv can be installed by: pip3 install virtualenv"
	rm -rf venv
	virtualenv -p $(PYTHON) venv
	source venv/bin/activate;\
	$(PIP) install notion-py;\
	$(PYTHON) --version;\
	$(PIP) --version;\
	$(PIP) install -r requirements.txt;
	echo "Active the virtual env: source venv/bin/activate"
	echo "Deactive when done: deactivate"

run:
	source venv/bin/activate;\
	$(PYTHON) main.py

docker-build:
	docker build -f ./Dockerfile -t $(DOCKER_IMAGE):$(DOCKER_VERSION) .

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down -v
