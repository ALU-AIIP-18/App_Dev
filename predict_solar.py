# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 08:37:38 2020

@author: rbisa
"""
from weather_API_solar import df_solar
import pickle
import pandas as pd

#pickle file loading solar
#with open(r"C:\Users\rbisa\anaconda3\envs\appdevenv\App_Dev_Summative\model.pkl", 'rb') as file_in:
#    s_model = pickle.load(file_in)
#    file_in.close()

s_model = pickle.load(open('model.pkl', 'rb'))

#df_solar_no_day = df_solar.drop(['Date, ] axis=1)    
#model prediction using imported dataframe with historical weather
#print(df_solar)
#df_solar_2 = df_solar
#print(df_solar_2)
#w_features = df_solar.drop(['Date'], axis=1)
df_solar_2 = df_solar.copy()
w_features = df_solar_2
predicted_power = s_model.predict(w_features)
    
#creating a df with the final predictions and weather for presentation; SOLAR_PRED
#df_solar_2 = df_solar
df_solar_2['Predicted_Solar'] = predicted_power
df_solar_2['Date'] = pd.date_range(start='09/13/2020',end='09/16/2020')
df_solar_2['Day'] = df_solar_2['Date'].dt.day
#print(df_solar_2)

#df_solar['Date'] = pd.date_range(start='09/09/2020',end='13/09/2020')