from flask import Flask, render_template, request
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from SRC.exception import CustomException
from SRC.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

##What is flask app and what is flask framework
"""A Flask app is a web application built using the Flask
 framework in the Python programming language. Flask is 
 a popular, lightweight web framework known for its
simplicity and flexibility [1]. """

'''The Flask framework is a "micro-framework" for Python, 
meaning it provides essential tools and features for 
building web applications without imposing a strict
structure or requiring specific libraries [1]. It is
designed to make getting started quickly and easily,
with the ability to scale up to complex applications. 

Key characteristics of the Flask framework include:
1. Minimalist: It starts with a simple core and allows
 developers to add extensions as needed for functionalities
 like database integration, form validation, and user
 authentication [1].
2. Werkzeug and Jinja2: It is based on the Werkzeug WSGI 
utility (Web Server Gateway Interface) for handling 
requests and responses, and the Jinja2 templating engine 
for rendering web pages [1].
3. Flexibility: It gives developers control over the 
application structure and the tools they want to use, 
making it ideal for both simple projects and prototypes, 
as well as complex services [1]'''

"""Rendering a web page means the browser interprets a 
website's code (HTML, CSS, JavaScript) and transforms it 
into the visual, interactive page you see and interact
 with on your screen, a step-by-step process involving 
 building models (DOM, CSSOM), creating a render tree, 
 calculating layout, and painting pixels. It's how code 
 becomes a functional website, crucial for speed, user 
 experience"""

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict_data', methods = ['GET', "POST"])
def predict_datapoint():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        data = CustomData(
            gender=request.form['gender'],
            race_ethnicity=request.form['ethnicity'],
            parental_level_of_education=request.form['parental_level_of_education'],
            lunch=request.form['lunch'],
            test_preparation_course=request.form['test_preparation_course'],
            reading_score=float(request.form['reading_score']),
            writing_score=float(request.form['writing_score'])
        )
        
        df = data.get_data_as_dataframe()
        print(df)
        print("Before prediction")
        predict_pipeline = PredictPipeline()
        print("mid prediction")
        results = predict_pipeline.predict(df)
        print("after prediction")
        return render_template("home.html", results= results[0])

if __name__ == "__main__":
 app.run(host="0.0.0.0", port=8080)
)
