all:
	latex biseccioncos.tex
	latex biseccioncos.tex
	bibtex biseccioncos
	latex biseccioncos.tex
	latex biseccioncos.tex
	dvips -o biseccioncos.ps biseccioncos.dvi
	ps2pdf -sPAPERSIZE=a4 -DMaxSubsetPct=100 -dCompatibilityLevel=1.2 -dSubsetFonts=true -dEmbedAllFonts=true biseccioncos.ps biseccioncos.pdf

clean:
	rm -f *.toc *.ps *.log *.lof *.lot *.dvi *.aux *.blg *.bbl
