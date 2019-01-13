RST=results

.PHONY: all clean

all: strip.png

clean :
	rm -f strip.png

strip.png : test/integration/valid.strip
	cd test/integration && ../../src/main.py valid.strip ../../strip.png

.PHONY : test pytest integration_tests pylint coverage
test : pytest integration_tests pylint 

pytest:
	py.test-3

integration_tests:
	rm -f test/integration/*.png
	cd test/integration && bats test.bats.sh

coverage:
	py.test-3 --cov=src --cov-report term-missing

pylint:
	pylint --rcfile=ci/pylintrc src/*.py src/*/*.py
