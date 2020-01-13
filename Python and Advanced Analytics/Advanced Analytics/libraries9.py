#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:07:07 2019

@author: student
"""
                        #Beautiful Soup

import requests
from bs4 import BeautifulSoup

response=requests.get('https://www.python.org/search/?q=dictionary&submit=')
if response.status_code==200:
    print('Successfull')
    #print(response.content)

else:
    print('Failed')

result_page=BeautifulSoup(response.content,'lxml')

print(result_page.prettify())

first_ul=result_page.find('ul',{'class':"list-recent-events menu"})
#first_li=first_a.find('li')
#first_h3=first_li.find('h3')

list_a=first_ul.find_all('a')
for a in list_a: 
    print(a.get_text())

#print(all_a_tags.text)
#print(type(all_a_tags))


                            #SELENIUM
    
    
#ERROR!!!!!!!!!!!!!!
                            
import sys
from selenium import webdriver
import time
import re


driver=webdriver.Firefox(executable_path='/home/student/Desktop/Python/Programs/Advanced Analytics/geckodriver')

#driver.get('https://python.org') 
driver.implicitly_wait(30)
driver.maximize_window()

driver.get('https://www.python.org/search/?q=List&submit=')

#search_field = driver.find_element_by_name('q')
#search_field.clear()
#
#search_field.send_keys('List')
#search_field.submit()

#lists=driver.find_elements_by_class_name('containe')
#print(Lists)

lists=driver.find_elements_by_tag_name('h3')


print('Found : '+ str(len(lists)) + ' searches: ')


i = 0
for listitem in lists:
    g = re.search('\>(.*)\<', listitem.get_attribute('innerHTML'))
    if g != None:    
        print(g.group(1))
    else:
        pass
    i=i+1
    if (i>10):
        break
     



driver=webdriver.Firefox(executable_path='/home/student/Desktop/Python/Programs/Advanced Analytics/geckodriver')


driver.implicitly_wait(30)
driver.maximize_window()

driver.get('https://www.google.com')

search_field = driver.find_element_by_name('q')
search_field.clear()

search_field.send_keys('Cdac')
search_field.submit()

lists=driver.find_elements_by_class_name("LC20lb")

print('Found : '+ str(len(lists)) + ' searches: ')


i = 0
for listitem in lists:
    print(listitem.get_attribute('innerHTML'))
    i=i+1
    if (i>10):
        break

















