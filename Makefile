PYTHON := python3
PIP := pip3

venv:
	rm -rf venv
	virtualenv -p $(PYTHON) venv
	source venv/bin/activate;\
		$(PIP) install notion-py;\
		$(PYTHON) --version;\
		$(PIP) --version;\
		$(PIP) install -r requirements.txt;
	@echo "Active the virtual env: source venv/bin/activate"
	@echo "Deactive when done: deactivate"