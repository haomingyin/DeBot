# install virtualenv and errbot
python3_path := $(shell which python3)

setup: 
	pip install virtualenv
	virtualenv --python $(python3_path) ./.venv
	./.venv/bin/pip install errbot
