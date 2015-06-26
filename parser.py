#!/usr/bin/python
#coding=utf-8
#Filename:parser.py
from config import *

def parse_cv(filename):
    """"""
    cursec = None
    curdict=[]
    ret = {}
    with open(filename, 'r') as fp:
        line = fp.readline()
        while line:
            line = line.strip()

            if not line:
                line = fp.readline()
                continue

            if line.startswith('['):
                if cursec:
                    ret[cursec] = curdict
                cursec = line.strip('[]')
                curdict = []
            elif not cursec:
                pos = line.find('=')
                key = line[:pos]
                value = line[pos + 1:]
                ret[key] = value
            else:
                values = line.split(grammar['separator'])
                curdict.append(values)

            line = fp.readline()

    if cursec:
        ret[cursec] = curdict

    return ret

if __name__ == '__main__':
    import pprint
    pprint.pprint (parse_cv('en.cv'))
