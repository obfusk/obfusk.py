SHELL = bash

.PHONY: all test test_verbose coverage clean

all:
	python3 setup.py sdist
	python3 setup.py bdist_wheel

test:
	python2 -mobfusk
	python3 -mobfusk
	pypy    -mobfusk

test_verbose:
	python2 -mobfusk -v
	python3 -mobfusk -v
	pypy    -mobfusk -v

coverage:
	python3 -mcoverage run -m obfusk
	python3 -mcoverage html

clean:
	rm -fr .coverage build/ dist/ htmlcov/ obfusk.egg-info/
	find -name '*.pyc' -delete
	find -name __pycache__ -delete
