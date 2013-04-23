requirements.txt: setup
	pip freeze \
	| sed -e '/Rigveda-Wiki-Mirror/d' -e '/gevent/d' \
	> requirements.txt
	cat static-requirements.txt >> requirements.txt

setup:
	python setup.py develop

.PHONY: setup requirements.txt
