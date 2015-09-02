cc=xelatex
tmp=*.log *.out *.aux *.pyc

all:resume-en.pdf resume-zh.pdf resume-zh-ad.pdf lili.pdf resume-en-other.pdf
again:
	$(cc) resume-zh.tex
	$(cc) resume-en.tex
	$(cc) resume-zh-ad.tex
	$(cc) lili.tex
	$(cc) resume-en-other.tex

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

lili.tex: resume-simple-template.tex lili.cv
	./gen.py $^ $@

lili.pdf: lili.tex config.tex
	$(cc) $<
	open $@

resume-en-other.pdf: resume-en-other.tex config.tex
	$(cc) $<
	open $@

.PHONY:clean
clean:
	-rm -f $(tmp)

.PHONY:distclean
distclean:
	-rm -f $(tmp) *.pdf
