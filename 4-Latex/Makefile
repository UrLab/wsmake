TARGET = rapport.pdf

all: ${TARGET}

clean:
	rm -f *.log *.aux *.out *.d

mrproper: clean
	rm -f ${TARGET}

%.eps: %.dia
	dia -e $@ $<

%.eps: %.dot
	dot -Teps $< > $@

%.pdf: %.tex
	pdflatex $<

%.d: %.tex
	./texdeps.sh $< > $@

include $(subst .pdf,.d,${TARGET})
