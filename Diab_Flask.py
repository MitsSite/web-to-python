# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:57:37 2021

@author: User"""

from flask import Flask,request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('Done_knn.pkl','rb'))
sc = pickle.load(open('knn_scaler.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(sc.transform(final_features))
    
    if(prediction == [0]):
        return render_template('index.html',msg = 'You Are Diabetes Freeeee!')
    else:
        return render_template('index.html',msg = 'You Are Diabetic, But It can be cured!')
    
if __name__ == "__main__":
    app.run()