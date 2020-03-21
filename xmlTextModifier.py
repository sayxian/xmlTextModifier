#!/usr/bin/env python

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

# Reads the first 20 lines, reads the xmlns attributes
ns = []
with open("sample.xml") as f:
    for lineIter in range(20):
        xmlstring = f.next()
        ns.append(return_all_match(xmlstring,re.compile(r'xmlns:[a-zA-Z0-9]*=\"[a-zA-Z0-9./:]*\"')))
    ns = set((filter(None,flatten(ns))))
    # print(ns)

tree = ET.parse('sample.xml')

# resets ET namespace in case there are other namespace created, which will override the previously created namespace
ET._namespace_map={}
for nsIter in ns:
    ET._namespace_map[return_first_match(nsIter,re.compile(r'\"[a-zA-Z0-9./:]*\"'))[1:-1]] = return_first_match(nsIter,r':[a-zA-Z]*=')[1:-1]
    # print(ET._namespace_map)

# implements simple lookup from list of args
#  to check if there is  ...arg / *argv in python 2.5
for bid in tree.findall(".//{http://www.example.com/schema/details}billToZipCode"):
    bid.text=str(random.random())

tree.write('sample1.xml')