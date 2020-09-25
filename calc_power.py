# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:59:45 2020

@author: rbisa
"""
import pandas as pd
from predict_wind import df_wind_2
from predict_solar import df_solar_2

#copies to be used in this module
df_wind_3 = df_wind_2.copy()
df_solar_3 = df_solar_2.copy()

d_sMSU = pd.read_csv(r"C:\Users\rbisa\anaconda3\envs\appdevenv\App_Dev\Uploads\solar_farm.csv", index_col=None)
#print(d_sMSU)
#y = d_sMSU.info()
#print(y)

#renaming columns
df_ss = d_sMSU.copy()

#conversion to numeric
#d_sMSU['Date Of Month'] = pd.to_numeric(d_sMSU['Date Of Month'], downcast="integer")
#d_sMSU['Capacity Available'] = pd.to_numeric(d_sMSU['Capacity Available'], downcast="integer")

#renaming columns to match df_solar
df_ss = df_ss.reindex(d_sMSU.index.drop(0)).reset_index(drop=True)
df_ss.columns = ['Day', 'Cap']
#print(df_ss)

#conversion to integer
df_ss['Day'] = df_ss['Day'].astype(int)
df_ss['Cap'] = df_ss['Cap'].astype(int)

#df_wind_3['Date'] = df_wind_3['Date'].astype(int)
df_wind_3['Day'] = df_wind_3['Day'].astype(int)

#df_solar_3['Date'] = df_solar_3['Date'].astype(int)
df_solar_3['Day'] = df_solar_3['Day'].astype(int)

power_df = pd.merge(df_solar_3, df_wind_3, on=['Date'])

power_df_final = power_df.drop(['Day_x'], axis=1)      #remember to remove suffix, seen solution on stack overflow
power_df_final.set_index("Date", inplace = True)

#print (power_df_final)

