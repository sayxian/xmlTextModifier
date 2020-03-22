#!/usr/bin/env python
'''
runs the code as 
./xmlTextModifier.py <xmlfile> <decimal places> <prefix:tag> <prefix:tag>

'''
from __future__ import with_statement
import xml.etree.ElementTree as ET
import sys
import random
import re

random.seed(1)

def return_first_match(text,regPattern):
    try:
        result = re.findall(regPattern,text)[0]
    except Exception, IndexError:
        result = ''
    return result

def return_all_match(text,regPattern):
    try:
        result = re.findall(regPattern,text)
    except Exception, IndexError:
        result = ''
    return result

def flatten(input):
    new_list = []
    for i in input:
        for j in i:
            new_list.append(j)
    return new_list

def lookupParser(input,namespace_array):
    if ":" in input:
        prefix, tag = input.split(':')
        # python 2 namespace_array.iteritems()
        for key,value in namespace_array.items():
            if (prefix==value):
                return ''.join('.//'+'{'+key+'}'+tag)
    # input is good; doesn't contain namespace, hence doesn't require transformation
    else:
        return input
# Reads the first 20 lines, reads the xmlns attributes
ns = []
with open(sys.argv[1]) as f:
    for lineIter in range(20):
        xmlstring = f.next()
        ns.append(return_all_match(xmlstring,re.compile(r'xmlns:[a-zA-Z0-9]*=\"[a-zA-Z0-9./:]*\"')))
    ns = set((filter(None,flatten(ns))))
    # print as python3 method to test namespace generated
    #  print(ns)

tree = ET.parse(sys.argv[1])

# resets ET namespace in case there are other namespace created, which will override the previously created namespace
ET._namespace_map={}
for nsIter in ns:
    ET._namespace_map[return_first_match(nsIter,re.compile(r'\"[a-zA-Z0-9./:]*\"'))[1:-1]] = return_first_match(nsIter,r':[a-zA-Z]*=')[1:-1]
# print(ET._namespace_map)

# implements simple lookup from list of args

# sets decimal for file
prec = int(sys.argv[2])

for sysValues in sys.argv[3:]:
    for lookupValue in tree.findall(lookupParser(sysValues,ET._namespace_map)):
        # used string manipulation instead of Decimal to convert to decimal places
        lookupValue.text=str(random.random())[:prec+2]

tree.write('sample1.xml')