# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:02:18 2020

@author: rbisa
"""
import pandas as pd
#import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
#from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
#from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#loading the data for analysis
wind_data = pd.read_csv(r'C:\Users\rbisa\anaconda3\envs\appdevenv\App_Dev\wind_generation_data.csv')

#cleaning the data
x_wind = wind_data.isnull().sum(axis=0) 
#print(x_wind)

#adding date column to wind dataframe
wind_data['Date'] = pd.date_range(start='1/1/2016', periods=len(wind_data), freq='D')

#checking datatypes
#y_wind = wind_data.info()

#ML modelling: XGBoost 
dataset2 = wind_data.drop(['Power Output', 'Date'], axis=1)
X_wind = dataset2.values
y_wind = wind_data['Power Output'].values

#data splitting

X_train, X_test, y_train, y_test = train_test_split(X_wind, y_wind, test_size=0.3, random_state=42)

#data transformation (scaling)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#creation of regressor model

forest_model2 = RandomForestRegressor(n_jobs=-1)

#fitting model
forest_model2.fit(X_train, y_train) # fit model

#predicting
y_predicted_w = forest_model2.predict(X_test)


#accuracy determination of random forest regression
score2 = r2_score(y_test, y_predicted_w)


#pickling
#with open(r"C:\Users\rbisa\anaconda3\envs\appdevenv\App_Dev_Summative\model_w.pkl", 'wb') as in_file:
#    pickle.dump(forest_model2, in_file)
#    in_file.close()
    
pickle.dump(forest_model2, open('model_w.pkl','wb'))