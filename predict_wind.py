# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 08:30:35 2020

@author: rbisa
"""
from weather_API import df_wind
import pickle
import pandas as pd

#pickle file loading wind
#with open(r"C:\Users\rbisa\anaconda3\envs\appdevenv\App_Dev_Summative\model_w.pkl", 'rb') as out_file:
#    w_model = pickle.load(out_file)
#    out_file.close()  

w_model = pickle.load(open('model_w.pkl', 'rb'))

    
#print(df_wind)
#model prediction using imported dataframe with historical weather from weatherbit.io
df_wind_2 = df_wind.copy()
w_features2 = df_wind_2
predicted_power_wind = w_model.predict(w_features2)
    
    #creating a df with the final predictions and weather for presentation; SOLAR_PRED
df_wind_2['Predicted_Wind'] = predicted_power_wind
df_wind_2['Date'] = pd.date_range(start='09/13/2020',end='09/16/2020')
df_wind_2['Day'] = df_wind_2['Date'].dt.day
#print(df_wind)    