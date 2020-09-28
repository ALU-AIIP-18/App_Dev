# App_Dev_Summative: 4-Day Power Output (MW) Forecast

This is the repository created by REBECCA MUTESI BISANGWA containing the AIIP App Dev Summative 2020. 

Weather API
Website used: weatherbit.io
range of historical dates used = 08/09/2020 - 12/09/2020

.py files
1. weather_API.py and weather_API_solar.py        
2. model_solar.py and model_wind.py
3. predict_solar.py and predict_wind.py
4. calc_power.py for scaling predicted solar power by solar maintenance schedule; solar_farm.csv was edited to reflect the 4 historical weather APIs and one date of the month to coincide with the predicted, to test this .py file. Attached edited file in repo.
5. my_dash_code.py 

6. routes.py ties them all together; ran in command prompt and starts up the web app to display everything

Web app extensions
1. '/' --> Home Page
2. '/MSUSolar' --> Solar Maintenance File Page
3. '/SolarPowerPrediction' --> 4-day Solar Power Output Forecast (MW)
4. '/WindPowerPrediction' --> 4-day Wind Power Output Forecast (MW)
5. '/dashdisplay/' --> Dashboard display of 4-day power forecast of solar and wind PPs
6. 'call_back' --> re-routing to Home Page
