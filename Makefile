requirements.txt: setup
	pip freeze > requirements.txt
setup:
	python setup.py develop

.PHONY: setup requirements.txt
