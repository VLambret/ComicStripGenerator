RST=results

.PHONY: all clean test unittest pylint

all: strip.png

clean :
	rm -f strip.png

%.png : %.comic
	python3 src/main.py -f $<

test : unittest pylint

unittest:
	nosetests3 --all-modules

pylint:
	pylint --rcfile=ci/pylintrc src/*.py src/*/*.py
