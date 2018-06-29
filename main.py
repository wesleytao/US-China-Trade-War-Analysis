#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:57:03 2018

@author: Keran
"""
from flask import Flask, flash, redirect, render_template, request, session, abort
#from flask_uploads import UploadSet, configure_uploads, IMAGES
import model
import io
import matplotlib.pyplot as plt
import base64



app = Flask(__name__)
@app.route("/")
def index():
    with open("input.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return render_template('input.html',plot_url=encoded_string)

@app.route('/', methods=[ 'POST'])
def make_prediction():
    if request.method=='POST':file = request.form['text']
    if not file: return render_template('input.html', label="No file")
    prediction = model.sentiment_analysis(file)
    img = io.BytesIO()
    plt.clf()
    plt.bar(range(len(prediction)), list(prediction.values()), align='center',
            color=["#56B4E9",'#d9d9d9','#ff8080','#00b3b3'])
    plt.xticks(range(len(prediction)), list(prediction.keys()))
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template('input.html', plot_url=plot_url)


if __name__ == '__main__':
	# load ml model
	#model = 
	# start api
	app.run(debug=True)