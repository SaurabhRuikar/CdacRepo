#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 14:21:07 2019

@author: student
"""

import sys
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path = '/home/student/Desktop/Python/Programs/Advanced Analytics/geckodriver')
driver.get()