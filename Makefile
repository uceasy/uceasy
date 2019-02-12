all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && venv/bin/python setup.py develop

run-web: venv
	FLASK_APP=web UCEASY_SETTINGS=../settings.cfg venv/bin/flask run

run-cli: venv
	python -c 'from cli.uceasy_cli import uceasy; uceasy()'

test: venv
	UCEASY_SETTINGS=../settings.cfg venv/bin/pytest

sdist: venv test
	venv/bin/python setup.py sdist
