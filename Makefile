RST=results
SRC=sources

.PHONY: all clean test

all: ${RST}/strip.png

test: stack_test

clean :
	rm -f $(RST)/*

${RST}/strip.png: ${RST}/panel.png \
                  ${RST}/bubble_pos.png
	./scripts/stack.sh $^ $@

${RST}/panel.png: $(SRC)/background.png \
                  $(SRC)/perso1.png \
                  $(SRC)/perso2.png
	./scripts/stack.sh $^ $@

${RST}/bubble_pos.png: ${RST}/bubble.png
	./scripts/pos.sh $< 350 100 1024 768 $@

${RST}/bubble.png: ${RST}/bubble.svg
	convert $< $@

${RST}/bubble.svg : Makefile
	./scripts/balloon.py -x 0 -y 0 -offset 40 -bx -50 -by -35 -c "Hi !" > $@

stack_test:
	./scripts/stack.sh sources/background.png sources/perso1.png sources/perso2.png results/stack_test1.png
	./scripts/stack.sh sources/background.png sources/perso1.png results/stack_test2.png
