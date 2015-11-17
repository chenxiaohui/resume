#!/usr/bin/python
#coding=utf-8
#Filename:parser.py

from config import *
import re
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
                curdict.append(values)
                #if len(values) > 1:
                    #tmp = [values[0]]
                    #tmp.extend(re.split('。|\|', values[1], 0))
                    #curdict.append(values)
                #else:
                    #curdict.append(values)

            line = fp.readline()

    if cursec:
        ret[cursec] = curdict

    return ret



if __name__ == '__main__':
    import pprint
    pprint.pprint(parse_cv('yangxing.cv'))
