#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:36:38 2019

@author: student
"""

class SalaryException(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg