all: homework06.pdf

homework06.pdf: homework06.tex ethnicity.png gender.png
	pdflatex homework06.tex

gender.png: gender.dat gender.plt
	gnuplot ./gender.plt

ethnicity.png: ethnicity.dat ethnicity.plt
	gnuplot ./ethnicity.plt

gender.dat: gender.sh
	./gender.sh > gender.dat

ethnicity.dat: ethnicity.sh
	./ethnicity.sh > ethnicity.dat

clean:
	rm -f homework06.pdf gender.png ethnicity.png
