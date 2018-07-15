# install virtualenv and errbot
python3_path := $(shell which python3)
# python3_path := $(shell pyenv which python3)

setup: 
	pip install virtualenv
	virtualenv --python $(python3_path) ./.venv
	./.venv/bin/pip install errbot
	mkdir -p ./data

text:
	./.venv/bin/errbot -T

start:
	./.venv/bin/errbot