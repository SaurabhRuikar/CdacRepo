#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:08:43 2019

@author: student
"""
from selenium import webdriver

driver = webdriver.Firefox(executable_path = '/home/student/Desktop/Python/Programs/Advanced Analytics/geckodriver')
driver.get('https://www.shopclues.com/?ef_id=EAIaIQobChMIt8vYiYnY5gIVDCQrCh1-gwMOEAAYASAAEgJWfPD_BwE:G:s&s_kwcid=AL!725!3!332655616938!e!!g!!shopclues&mcid=ps&utm_source=Google&utm_medium=cpc&utm_campaign=Search_Text_Exact_Brand_Shopclues')

s = driver.find_element_by_name('q')
s.send_keys('shoes')
s.submit()

driver.implicitly_wait(20)
#lst = driver.find_elements_by_class_name('')
lst1=driver.find_elements_by_class_name('textContainer_text')

for i in lst1:
        print("Name:"+i.get_attribute("innerHTML"))
        #print(i.get_attribute("innerHTML"))
        print()
        print()
