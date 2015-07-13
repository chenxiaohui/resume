cc=xelatex
tmp=*.log *.out *.aux

all:resume-en.pdf resume-zh.pdf resume-zh-ad.pdf
again:
	$(cc) resume-zh.tex
	$(cc) resume-en.tex
	$(cc) resume-zh-ad.tex

resume-zh.tex: resume-zh-template.tex zh.cv
	./gen.py $^ $@

resume-zh.pdf:resume-zh.tex config.tex
	$(cc) $<
	open $@

resume-en.tex: resume-en-template.tex en.cv
	./gen.py $^ $@

resume-en.pdf:resume-en.tex config.tex
	$(cc) $<
	open $@

resume-zh-ad.tex: resume-zh-template.tex zh-ad.cv
	./gen.py $^ $@

resume-zh-ad.pdf: resume-zh-ad.tex config.tex
	$(cc) $<
	open $@

.PHONY:clean
clean:
	-rm -f $(tmp)

.PHONY:distclean
distclean:
	-rm -f $(tmp) *.pdf
