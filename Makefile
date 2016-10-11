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

%.png: %.svg
	convert $< $@

###############################################################################
# PANEL 1
###############################################################################

${RST}/panel1_pos.png: ${RST}/panel1.png
	./scripts/pos.sh $< 0 0 1024 2304 $@

${RST}/panel1.png: ${RST}/panel.png ${RST}/bubble1_pos.png
	./scripts/stack.sh $^ $@

${RST}/bubble1_pos.png: ${RST}/bubble1.png
	./scripts/pos.sh $< 350 100 1024 768 $@

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
	./scripts/pos.sh $< 550 100 1024 768 $@

${RST}/bubble2.svg : Makefile
	./scripts/balloon.py -x 0 -y 0 -offset 40 -bx 150 -by -35 -c "Hi" > $@

###############################################################################
# PANEL 3
###############################################################################

${RST}/panel3_pos.png: ${RST}/panel3.png
	./scripts/pos.sh $< 0 1536 1024 2304 $@

${RST}/panel3.png: ${RST}/panel.png ${RST}/bubble3_left_pos.png ${RST}/bubble3_rigth_pos.png
	./scripts/stack.sh $^ $@

${RST}/bubble3_left_pos.png: ${RST}/bubble3_left.png
	./scripts/pos.sh $< 250 10 1024 768 $@

${RST}/bubble3_left.svg : Makefile
	./scripts/balloon.py -x 0 -y 0 -offset 100 -bx -50 -by -35 -c "Will Eisner award is" "not for today..." > $@

${RST}/bubble3_rigth_pos.png: ${RST}/bubble3_rigth.png
	./scripts/pos.sh $< 550 120 1024 768 $@

${RST}/bubble3_rigth.svg : Makefile
	./scripts/balloon.py -x 0 -y 0 -offset 150 -bx 250 -by -35 -c "Next time maybe ?" > $@

###############################################################################
# TESTS
###############################################################################

stack_test:
	./scripts/stack.sh sources/background.png sources/perso1.png sources/perso2.png results/stack_test1.png
	./scripts/stack.sh sources/background.png sources/perso1.png results/stack_test2.png
