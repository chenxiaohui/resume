#!/usr/bin/python
#coding=utf-8
#Filename:gen.py

import sys
from config import *
from parser import parse_cv


def render(filename, context = {}):
    """"""
    try:
        with open(filename, 'r') as fp:
            text = fp.read()
    except Exception:
        raise
    hit = pattern.search(text)
    output = ''
    lastpos = 0
    while hit:
        start, end = hit.span()
        output += text[lastpos:start]
        key = hit.groups()[0]
        if key.startswith(grammar['for']):
            section = key[len(grammar['for']):]
            if section in context.keys():
                tmplen, tmpout = render_for(text[end + 1:], context[section])
            else:
                raise Exception
            output += tmpout
            lastpos = end + tmplen + 1
        else:
            if key in context.keys():
                 output += context[key]
            lastpos = end
        hit = pattern.search(text, lastpos)

    output += text[lastpos:]
    return output

def render_for(text, context = {}):
    """"""
    tmplen = 0
    output = ''
    hit = pattern.search(text)
    if hit:
        start, end = hit.span()
        key = hit.groups()[0]
        if key == grammar['endfor']:
            tmplen = end
            body = text[:start]
            #precompile
            template = precompile(body)
            for record in context:
                if isinstance(record, list):
                    orders=[str(i) for i in range(0, 0 + len(record))]
                    record = dict(zip(orders, record))
                output += template % record
        else:
            raise Exception
    else:
        raise Exception
    return tmplen, output

def precompile(text):
    """"""
    lastpos = 0
    output = ''
    hit = sub_pattern.search(text, lastpos)
    while hit:
        beg, end = hit.span()
        key = hit.groups()[0]
        output += text[lastpos:beg] + '%(' + key + ')s'
        lastpos = end
        hit = sub_pattern.search(text, lastpos)

    output += text[lastpos:]
    return output

def help():
    """"""
    print "./gen.py <template-file> <cvfile> <output-file>"

if __name__ == '__main__':
    if len(sys.argv) < 4:
        help()
        exit()
    else:
        template_file = sys.argv[1]
        cv_file = sys.argv[2]
        output_file = sys.argv[3]

    context = parse_cv(cv_file)
    output = render(template_file, context)
    with open(output_file, 'w') as fp:
        fp.write(output)

#if __name__ == '__main__':
    #context = parse_cv('zh.cv')
    #output = render('resume-en-template.tex', context)
    #print output
