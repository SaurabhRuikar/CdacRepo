#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:53:58 2019

@author: student
"""

import scrapy

class BrickSetSpider(scrapy.Spider):
    name="brickset spider"
    start_urls=["http://brickset.com/sets/year-2016"]

    def parse(self,response) :
        SET_SELECTOR='.set'
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR='h1 ::text'
            yield{
                    'name':brickset.css(NAME_SELECTOR).extract_first(),
                    }        
    
