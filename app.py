from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('random_forest_regressor.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        year = int(request.form["Year"])
        present_price = float(request.form["present_price"])
        kms_driven = int(request.form["km_driven"])
        Owner = int(request.form["Owner"])
        Fuel_type_petrol = request.form["Fuel_type_petrol"]
        if (Fuel_type_petrol == 'Petrol'):
            Fuel_type_petrol = 1
            Fuel_type_diesel = 0

        else:
            Fuel_type_petrol = 0
            Fuel_type_diesel = 1

        Year = 2022 - year
        Seller_Type_Individual = request.form['Seller_type']
        if (Seller_Type_Individual == 'Individual'):
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0

        Transmission_Mannual = request.form['Transmission_type']
        if (Transmission_Mannual == 'Manual'):
            Transmission_Mannual = 1
        else:
            Transmission_Mannual = 0

        prediction = model.predict([[Year, present_price, kms_driven, Owner,  Fuel_type_petrol, Fuel_type_diesel, Seller_Type_Individual, Transmission_Mannual ]])
        output = round(prediction[0],2)
        if output < 0:
            return render_template('index.html', prediction_text = "Sorry you cannot sell the car")
        else:
            return render_template('index.html', prediction_text="you can sell the car at {}".format(output))

if __name__=="__main__":
    app.run(debug=True)

