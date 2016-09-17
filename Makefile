RST=results
SRC=sources

.PHONY: all clean

all: $(RST)/result.png

clean :
	rm -f $(RST)/*

$(RST)/result.png : $(RST)/tmp.png
	composite $(SRC)/perso2.png $< $@

$(RST)/tmp.png:
	composite $(SRC)/perso1.png $(SRC)/background.png $@
