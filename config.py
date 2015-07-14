#!/usr/bin/python
#coding=utf-8
#Filename:config.py
import re

grammar = {
    'for':'for=>',
    'endfor':'endfor',
    'separator':'|'
}
regex = {
    'default':'%(\S+?)%',
    'subvariable':'\{(\d+?)\}'
}

pattern = re.compile(regex['default'])
sub_pattern = re.compile(regex['subvariable'])
