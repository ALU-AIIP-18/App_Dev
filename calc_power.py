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

df_ss = d_sMSU.copy()

#renaming columns to match df_solar
df_ss = df_ss.reindex(d_sMSU.index.drop(0)).reset_index(drop=True)
df_ss.columns = ['Day', 'Cap']

#conversion to integer
df_ss['Day'] = df_ss['Day'].astype(int)
df_ss['Cap'] = df_ss['Cap'].astype(int)

#df_wind_3['Date'] = df_wind_3['Date'].astype(int)
df_wind_3['Day'] = df_wind_3['Day'].astype(int)

#df_solar_3['Date'] = df_solar_3['Date'].astype(int)
df_solar_3['Day'] = df_solar_3['Day'].astype(int)

#merging and recalculating solar power output
merge_solar = pd.merge(df_solar_3, df_ss, on=['Day'])
merge_solar['Predicted_Solar'] = merge_solar['Predicted_Solar'] * merge_solar['Cap']/100
final_solar = pd.merge(df_solar_3, merge_solar, how = 'outer', on=['Day'],suffixes = ('_', ''))

#dropping off cap column 
final_solar_2 = final_solar.drop(['Cap'], axis=1)

#columns handling; ref for this section: peer consulation --> Abimbola 
new_cols = final_solar_2.columns[final_solar_2.columns.str.endswith('_')]
former_cols = new_cols.str[:-1]

#creating columns dictionary to work with when filtering out the NaNs, appending   
eff = dict(zip(new_cols, former_cols))

#removing the NaNs/NaTs
final_solar_2[former_cols] = final_solar_2[former_cols].combine_first(final_solar_2[new_cols].rename(columns=eff))
final_solar_2 = final_solar_2.drop(new_cols, axis=1)

power_df = pd.merge(final_solar_2, df_wind_3, on=['Date'])

power_df_final = power_df.drop(['Day_x'], axis=1)
power_df_final['Total_Predicted_Power'] = power_df_final['Predicted_Solar'] + power_df_final['Predicted_Wind']
power_df_final.set_index("Date", inplace = True)


