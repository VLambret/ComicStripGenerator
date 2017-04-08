RST=results

.PHONY: all clean test

all: strip.png

clean :
	rm -f strip.png

%.png : %.comic
	python3 src/main.py -f $<

pylint:
	pylint --rcfile=ci/pylintrc src/*.py
