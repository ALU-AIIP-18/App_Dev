# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:29:08 2020

@author: rbisa
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:57:52 2020

@author: rbisa
"""

from flask import Flask, request, jsonify, render_template, redirect
from predict_solar import df_solar_2
from predict_wind import df_wind_2
import os
import my_dash_code

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#flask and dash instantiation
server = Flask(__name__)   
app = my_dash_code.get_dash(server)


#route 1: "Home Page"
@app.server.route('/')
def home():
    return render_template('home_page.html')

#route 2: MSU = Maintenance Schedule Upload Page for Solar
@app.server.route('/MSUSolar', methods = ['POST', 'GET']) 
def uploader():
    if request.method == "POST":
        csv_file = request.files['file']
        csv_file.save(os.path.join("Uploads", csv_file.filename))

    return render_template('solar_csv_upload.html')
    
#route 3: solar PP model
@app.server.route('/SolarPowerPrediction', methods = ['POST', 'GET']) #MSU = Maintenance Schedule Upload Page
def predict():    
    
    #conversion to list
    solar = df_solar_2['Predicted_Solar']
    sol_list = solar.tolist()
    
    #rounding off
    sol_list = [round(i, 2) for i in sol_list]

    return jsonify(sol_list)
    
#route 4: wind PP model
@app.server.route('/WindPowerPrediction', methods = ['POST', 'GET'])
def predict_wind():
    
   #jasonifying the output to be returned
    wind = df_wind_2['Predicted_Wind']
    wind_list = wind.tolist()
    
    #rounding off
    wind_list = [round(i, 2) for i in wind_list]
    
    return jsonify(wind_list)
    
    
#route 5: DASH layout
@app.server.route("/call_back")
def call_back():
    print("Re-routing to Home Page...")
    
    return redirect("/")

@app.server.route("/store_file")
def store_file():
    keep = request.files.get("filename", None)
    if keep:
        print(keep.stream.read())
    
    return redirect("/")


if __name__ == '__main__':
    app.run_server(debug=True)