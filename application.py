# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:33:16 2023

@author: aspdi
"""

from flask import Flask, request

import joblib

model=joblib.load(r"bbc_model.pkl")
target_encoder=joblib.load(r"target_encoder.pkl")
tf_idf_encoder=joblib.load(r"tf-idf_encoder.pkl")


app=Flask(__name__)

@app.route('/',methods=['POST'])

def prediction():
    data=request.get_json('test')
    data=data['test']
    en_data=tf_idf_encoder.transform(data)
    en_data=en_data.toarray()
    out=model.predict(en_data)
    output=target_encoder.inverse_transform(out)
    return str(output)
