RST=results
SRC=sources

.PHONY: all clean

all: $(RST)/result.png

clean :
	rm -f $(RST)/*

$(RST)/result.png : $(RST)/tmp2.png $(RST)/speechBubble.png
	composite $(RST)/speechBubble.png $< $@

$(RST)/tmp2.png : $(RST)/tmp.png
	composite $(SRC)/perso2.png $< $@

$(RST)/tmp.png:
	composite $(SRC)/perso1.png $(SRC)/background.png $@

$(RST)/speechBubble.png : $(SRC)/speechBubble.svg
	convert $< $@
