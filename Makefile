RST=results
SRC=sources

.PHONY: all clean test

all: ${RST}/strip.png

test: stack_test

clean :
	rm -f $(RST)/*

${RST}/strip.png: ${RST}/panel.png
	cp $^ $@

${RST}/panel.png: $(SRC)/background.png \
                  $(SRC)/perso1.png \
                  $(SRC)/perso2.png
	./scripts/stack.sh $^ $@

stack_test:
	./scripts/stack.sh sources/background.png sources/perso1.png sources/perso2.png results/stack_test1.png
	./scripts/stack.sh sources/background.png sources/perso1.png results/stack_test2.png
