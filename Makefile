RST=results
SRC=sources

.PHONY: all clean test

all: ${RST}/strip.png

test: stack_test

clean :
	rm -f $(RST)/*

${RST}/strip.png: ${RST}/panel1_pos.png \
                  ${RST}/panel2_pos.png \
                  ${RST}/panel3_pos.png
	./scripts/stack.sh $^ $@

${RST}/panel.png: $(SRC)/background.png \
                  $(SRC)/perso1.png \
                  $(SRC)/perso2.png
	./scripts/stack.sh $^ $@

###############################################################################
# PANEL 1
###############################################################################

${RST}/panel1_pos.png: ${RST}/panel1.png
	./scripts/pos.sh $< 0 0 1024 2304 $@

${RST}/panel1.png: ${RST}/panel.png ${RST}/bubble1_pos.png
	./scripts/stack.sh $^ $@

${RST}/bubble1_pos.png: ${RST}/bubble1.png
	./scripts/pos.sh $< 350 100 1024 768 $@

${RST}/bubble1.png: ${RST}/bubble1.svg
	convert $< $@

${RST}/bubble1.svg : Makefile
	./scripts/balloon.py -x 0 -y 0 -offset 40 -bx -50 -by -35 -c "Hi !" > $@

###############################################################################
# PANEL 2
###############################################################################

${RST}/panel2_pos.png: ${RST}/panel2.png
	./scripts/pos.sh $< 0 768 1024 2304 $@

${RST}/panel2.png: ${RST}/panel.png ${RST}/bubble2_pos.png
	./scripts/stack.sh $^ $@

${RST}/bubble2_pos.png: ${RST}/bubble2.png
	./scripts/pos.sh $< 350 100 1024 768 $@

${RST}/bubble2.png: ${RST}/bubble2.svg
	convert $< $@

${RST}/bubble2.svg : Makefile
	./scripts/balloon.py -x 0 -y 0 -offset 40 -bx -50 -by -35 -c "Hi !" > $@

###############################################################################
# PANEL 3
###############################################################################

${RST}/panel3_pos.png: ${RST}/panel3.png
	./scripts/pos.sh $< 0 1536 1024 2304 $@

${RST}/panel3.png: ${RST}/panel.png ${RST}/bubble3_pos.png
	./scripts/stack.sh $^ $@

${RST}/bubble3_pos.png: ${RST}/bubble3.png
	./scripts/pos.sh $< 350 100 1024 768 $@

${RST}/bubble3.png: ${RST}/bubble3.svg
	convert $< $@

${RST}/bubble3.svg : Makefile
	./scripts/balloon.py -x 0 -y 0 -offset 40 -bx -50 -by -35 -c "Hi !" > $@

###############################################################################
# TESTS
###############################################################################

stack_test:
	./scripts/stack.sh sources/background.png sources/perso1.png sources/perso2.png results/stack_test1.png
	./scripts/stack.sh sources/background.png sources/perso1.png results/stack_test2.png
