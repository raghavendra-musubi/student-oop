#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:29:03 2020

@author: musubidm
"""

import os
from collections import OrderedDict


path = '/Users/musubidm/Documents/'
filename = 'test.csv'
delim = ','
header = True


#os.chdir(path)
file = open(path + filename)

raw = file.readlines()

header = raw[0]

data = raw[1:]

csv = OrderedDict()

header = header[:-1]
header = header.split(',')

for col in header:
    csv[col] = []
    
for row in data:
    row = row[:-1]
    row  = row.split(',')
    print(row)
    for col, val in zip(csv.keys(), row):
        csv[col].append(val)
        


    



