all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && venv/bin/python setup.py develop

run-web: venv
	FLASK_APP=uceasy UCEASY_SETTINGS=../settings.cfg venv/bin/flask run

run-cli: venv
	python cli/uceasy_cli.py

test: venv
	UCEASY_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist: venv test
	venv/bin/python setup.py sdist
