# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:54:06 2020

@author: rbisa
"""
#from app import app
import pandas as pd
import requests
import json
import datetime as dt
#import numpy as np

    #API Key for weatherbit.io = 0b43a42b572e41d5b1435c7870508c387
    #longitude = 53.556563, latitude = 8.598084

u_url = 'https://api.weatherbit.io/v2.0/history/daily?&lat=8.598084&lon=53.556563&start_date=2020-09-08&end_date=2020-09-09&key=0b43a42b572e41d5b1435c7870508c38'
u_url_2 = 'https://api.weatherbit.io/v2.0/history/daily?&lat=8.598084&lon=53.556563&start_date=2020-09-09&end_date=2020-09-10&key=0b43a42b572e41d5b1435c7870508c38'
u_url_3 = 'https://api.weatherbit.io/v2.0/history/daily?&lat=8.598084&lon=53.556563&start_date=2020-09-10&end_date=2020-09-11&key=0b43a42b572e41d5b1435c7870508c38'
u_url_4 = 'https://api.weatherbit.io/v2.0/history/daily?&lat=8.598084&lon=53.556563&start_date=2020-09-11&end_date=2020-09-12&key=0b43a42b572e41d5b1435c7870508c38'


#historical day 1
weather_data = requests.get(u_url).json()['data'][0]['wind_spd']   
w_drc = requests.get(u_url).json()['data'][0]['wind_dir']

#historical day 2
weather_data_2 = requests.get(u_url_2).json()['data'][0]['wind_spd']
w_drc_2 = requests.get(u_url_2).json()['data'][0]['wind_dir']

#historical day 3
weather_data_3 = requests.get(u_url_3).json()['data'][0]['wind_spd']
w_drc_3 = requests.get(u_url_3).json()['data'][0]['wind_dir']

#historical day 4
weather_data_4 = requests.get(u_url_4).json()['data'][0]['wind_spd']
w_drc_4 = requests.get(u_url_4).json()['data'][0]['wind_dir']

#adding values to a list
values = [weather_data, weather_data_2, weather_data_3, weather_data_4]
values2 = [w_drc, w_drc_2, w_drc_3, w_drc_4]

#converting to df
df_wind = pd.DataFrame(list(zip(values, values2)), 
               columns =['wind speed', 'direction'])  

#adding datetime
#df_wind['Date'] = pd.date_range(start='09/08/2020', end= '09/11/2020')
#df_wind['Day'] = df_wind['Date'].dt.day

#convert day to integer
#df_wind['Day'] = pd.to_numeric(df_wind['Day'], downcast="integer")

#print(df_wind)