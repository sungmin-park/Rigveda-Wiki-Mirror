requirements.txt: setup
	pip freeze | grep -v 'vamf12/Rigveda-Wiki-Mirror.git' > requirements.txt
	echo '-e .' >> requirements.txt

setup:
	python setup.py develop

.PHONY: setup requirements.txt
