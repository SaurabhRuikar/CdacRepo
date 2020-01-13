#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:02:09 2019

@author: student
"""

class WithdrawException(Exception):
    def __init__(self,msg):
        self.msg=msg
        
    def __str__(self):
        return self.msg
    