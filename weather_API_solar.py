# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:05:43 2020

@author: rbisa
"""
import pandas as pd
import requests
import json
import datetime as dt
#import numpy as np

    #API Key for weatherbit.io = 0b43a42b572e41d5b1435c7870508c387
    #longitude = 53.556563, latitude = 8.598084

s_url = 'https://api.weatherbit.io/v2.0/history/daily?&lat=-19.461907&lon=142.110216&start_date=2020-09-08&end_date=2020-09-09&key=0b43a42b572e41d5b1435c7870508c38'
s_url_2 = 'https://api.weatherbit.io/v2.0/history/daily?&lat=-19.461907&lon=142.110216&start_date=2020-09-09&end_date=2020-09-10&key=0b43a42b572e41d5b1435c7870508c38'
s_url_3 = 'https://api.weatherbit.io/v2.0/history/daily?&lat=-19.461907&lon=142.110216&start_date=2020-09-10&end_date=2020-09-11&key=0b43a42b572e41d5b1435c7870508c38'
s_url_4 = 'https://api.weatherbit.io/v2.0/history/daily?&lat=-19.461907&lon=142.110216&start_date=2020-09-11&end_date=2020-09-12&key=0b43a42b572e41d5b1435c7870508c38'
    
#historical day 1
temp_hi = requests.get(s_url).json()['data'][0]['max_temp']
temp_lo = requests.get(s_url).json()['data'][0]['min_temp']
solar_radi = requests.get(s_url).json()['data'][0]['solar_rad']
clouds = requests.get(s_url).json()['data'][0]['clouds']

#historical day 2
temp_hi_2 = requests.get(s_url_2).json()['data'][0]['max_temp']
temp_lo_2 = requests.get(s_url_2).json()['data'][0]['min_temp']
solar_radi_2 = requests.get(s_url_2).json()['data'][0]['solar_rad']
clouds_2 = requests.get(s_url_2).json()['data'][0]['clouds']

#historical day 3
temp_hi_3 = requests.get(s_url_3).json()['data'][0]['max_temp']
temp_lo_3 = requests.get(s_url_3).json()['data'][0]['min_temp']
solar_radi_3 = requests.get(s_url_3).json()['data'][0]['solar_rad']
clouds_3 = requests.get(s_url_3).json()['data'][0]['clouds']

#historical day 4
temp_hi_4 = requests.get(s_url_4).json()['data'][0]['max_temp']
temp_lo_4 = requests.get(s_url_4).json()['data'][0]['min_temp']
solar_radi_4 = requests.get(s_url_4).json()['data'][0]['solar_rad']
clouds_4 = requests.get(s_url_4).json()['data'][0]['clouds']

#list
s_values = [temp_hi, temp_hi_2, temp_hi_3, temp_hi_4]
s_values1 = [temp_lo, temp_lo_2, temp_lo_3, temp_lo_4]
s_values2 = [solar_radi, solar_radi_2, solar_radi_3, solar_radi_4]
s_values3 = [clouds, clouds_2, clouds_3, clouds_4]

#to df
df_solar = pd.DataFrame(list(zip(s_values, s_values1, s_values2, s_values3)), 
               columns =['tempHi', 'tempLow', 'Solar', 'CloudCoverPercentage'])

#datetime
#df_solar['Date'] = pd.date_range(start='09/08/2020', end= '09/11/2020')
#df_solar['Day'] = df_solar['Date'].dt.day

#convert day to int
#df_solar['Day'] = pd.to_numeric(df_solar['Day'], downcast="integer")

#print(df_solar)