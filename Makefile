cc=xelatex
tmp=*.log *.out *.aux

all:resume-en.pdf resume-zh.pdf
again:
	$(cc) resume-zh.tex
	$(cc) resume-en.tex

resume-zh.pdf:resume-zh.tex config.tex resume-zh-template.tex zh.cv
	./gen.py resume-zh-template.tex zh.cv resume-zh.tex
	$(cc) $<
	open $@

resume-en.pdf:resume-en.tex config.tex resume-en-template.tex en.cv
	./gen.py resume-en-template.tex en.cv resume-en.tex
	$(cc) $<
	open $@

.PHONY:clean
clean:
	-rm -f $(tmp)

.PHONY:distclean
distclean:
	-rm -f $(tmp) *.pdf
