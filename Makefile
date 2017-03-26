RST=results

.PHONY: all clean test

all: $(RST)/strip.png

clean :
	rm -f $(RST)/* strip.mk

$(RST)/strip.png : strip.mk
	make -f strip.mk -j 4

strip.mk : strip.comic
	make clean
	python3 src/main.py > $@
