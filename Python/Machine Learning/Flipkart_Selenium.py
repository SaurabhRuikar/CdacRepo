#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 14:45:04 2019

@author: student
"""

from selenium import webdriver

driver = webdriver.Firefox(executable_path = '/home/student/Desktop/Python/Programs/Advanced Analytics/geckodriver')
driver.get('https://www.flipkart.com/?gclid=EAIaIQobChMIlrSG9_7X5gIVgpCPCh3rbwE9EAAYASAAEgIkEPD_BwE&ef_id=EAIaIQobChMIlrSG9_7X5gIVgpCPCh3rbwE9EAAYASAAEgIkEPD_BwE:G:s&s_kwcid=AL!739!3!260659653813!e!!g!!flipkart&semcmpid=sem_8024046704_brand_eta_goog')
s = driver.find_element_by_name('q')
s.send_keys('mobile')
s.submit()

driver.implicitly_wait(20)
lst = driver.find_elements_by_class_name('_1vC4OE')
lst1=driver.find_elements_by_class_name('_3wU53n')

for i in lst:
    for k in lst1:
        print("Name:"+k.get_attribute("innerHTML"))
        print(i.get_attribute("innerHTML"))
        print()
        print()
    


