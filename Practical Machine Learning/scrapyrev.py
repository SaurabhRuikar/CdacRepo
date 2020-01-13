#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:18:10 2019

@author: student
"""
'''
import scrapy
#scrapy runspider scarpyrev.py in terminal windwo to run
class MyScraper(scrapy.Spider):
    name="flipkart spider"
    start_urls=['https://www.flipkart.com/audio-video/pr?sid=0pm&marketplace=FLIPKART&offer=nb:mp:11ec028425&fm=neo%2Fmerchandising&iid=M_0c8da7a0-488d-4c14-a4be-405c59d99ea7_2.KJCLZLP21NP5&ppt=browse&ppn=browse&ssid=0uvhyh6lw00000001577505487667&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_2.dealCard.OMU_KJCLZLP21NP5_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&cid=KJCLZLP21NP5']
    def parse(self,response) :
        SET_SELECTOR='._2cLu-l'
        Price_Selector='._1vC4OE'
        a_data=response.css(SET_SELECTOR).extract()
        p_data=response.css(Price_Selector).extract()
        for a,b in zip(a_data,p_data):
            NAME_SELECTOR='a ::text'
            Price_data='div ::text'
            yield{
                    'name':a.css(NAME_SELECTOR).extract_first(),
                    'Price':b.css(Price_data).extract_first(),
                    }        
'''

import scrapy
#scrapy runspider scarpyrev.py in terminal windwo to run
class MyScraper(scrapy.Spider):
    name="flipkart spider"
    start_urls=['http://www.know-it.co.in/Placement.aspx']
        SET_SELECTOR='padding-left:5px;padding-right:5px'
        #Price_Selector='._1vC4OE'
        a_data=response.css(SET_SELECTOR).extract()
        #p_data=response.css(Price_Selector).extract()
        for a in zip(a_data):
            NAME_SELECTOR='a ::text'
            #Price_data='div ::text'
            yield{
                    'name':a.css(NAME_SELECTOR).extract_first(),
                    #'Price':b.css(Price_data).extract_first(),

    