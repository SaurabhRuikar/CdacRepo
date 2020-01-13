#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:49:42 2019

@author: student
"""

import re
with open("Regexp1.txt") as fh1:
    with open("Regexp2.txt") as fh2:
        lst1=fh1.readlines()
        lst2=fh2.readlines()
        for ln1 in lst1:
            m1=re.match("(\d{3},.+?),",ln1,re.I)
            for ln2 in lst2:
                m2=re.match(m1.group(1),ln2,re.I)
                if m2!=None:
                    print(ln1)
                    print(ln2)
                
        