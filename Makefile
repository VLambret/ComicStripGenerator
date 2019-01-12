RST=results

.PHONY: all clean

all: strip.png

clean :
	rm -f strip.png

%.png : %.comic
	python3 src/main.py -f $<

.PHONY : test pytest integration_tests pyling coverage
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
