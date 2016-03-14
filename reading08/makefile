all: reading08.pdf

reading08.pdf: reading08.tex results.png
	pdflatex reading08.tex

results.png: results.dat histogram.plt
	gnuplot ./histogram.plt

clean:
	rm -f reading08.pdf results.png
