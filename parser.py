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

            if line.startswith('['): #new section
                if cursec:
                    ret[cursec] = curdict #commit last dict
                cursec = line.strip('[]')
                curdict = []
            elif not cursec: #default section
                pos = line.find('=')
                key = line[:pos]
                value = line[pos + 1:]
                ret[key] = value
            else: #in a section
                values = line.split(grammar['separator'])
                if len(values) > 1:
                    tmp = [values[0]]
                    tmp.extend(values[1].split('。', 1))
                    curdict.append(tmp)
                else:
                    curdict.append(values)

            line = fp.readline()

    if cursec:
        ret[cursec] = curdict

    return ret

if __name__ == '__main__':
    import pprint
    pprint.pprint (parse_cv('test.cv'))
