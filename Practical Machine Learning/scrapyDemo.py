#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:50:56 2019

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scrapy


class BrickSetSpider(scrapy.Spider):
    name = 'brickset spiider'
    start_urls = ['https://brickset.com/sets?query=2016']
    
    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h1 ::text'
            yield{'name':brickset.css(NAME_SELECTOR).extract_first(),}