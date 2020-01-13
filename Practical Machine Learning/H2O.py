#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:37:27 2019

@author: student
"""
'''
pip install  requests
pip install scikit-learn
pip install colorama
pip install future
pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o
'''
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
import h2o
h2o.init()
airlines_train_data=h2o.import_file("https://s3.amazonaws.com/h2o-airlines-unpacked/allyears2k.csv")


from h2o.estimators.gbm import H2OGradientBoostingEstimator

gbm_model=H2OGradientBoostingEstimator()
gbm_model.train(x=['Month','DayOfWeek','Distance'],y='IsArrDelayed',
                training_frame=airlines_train_data)
print(gbm_model)
gbm_model.predict(airlines_train_data)


from h2o.estimators.xgboost import H2OXGBoostEstimator

xgb_model=H2OXGBoostEstimator()
xgb_model.train(x=['Month','DayOfWeek','Distance'],y='IsArrDelayed',
                training_frame=airlines_train_data)
print(xgb_model)
xgb_model.predict(airlines_train_data)

