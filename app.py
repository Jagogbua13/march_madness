import os
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import warnings
warnings.simplefilter('ignore', FutureWarning)
import keras
from keras.models import load_model
from keras import backend as K

import Data_prep
from sklearn.externals import joblib

app = Flask(__name__)

#scaler = joblib.load("xscaler.save") 
#ncaa_model = load_model("deep_neural_ncaa_trained.h5")
def load_models():
    global model
    global graph
    model = load_model("deep_neural_ncaa_trained.h5")
    #graph = tf.get_default_graph()
    graph = K.get_session().graph

def load_scalar():
    global scalar
    scalar = joblib.load("xscaler.save") 

load_models()
load_scalar()
def model_predict(home,away):
    with graph.as_default():
        team_stats= Data_prep.model_prep(home,away)
        x_valid = scalar.transform(team_stats)
        prediction= model.predict(x_valid)
    
        result = np.argmax(prediction,axis=None,out=None)
        if result == 0 :
            answer = (f'{home} wins')
            loser = (f'{away}')
        else:
            answer= (f'{away} wins')
            loser = (f'{home}')
        results = {"winner":answer,"loser":loser}
    #return answer
    return (results)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/schools")
def get_schools():
    schools = Data_prep.school_list()
    return jsonify(schools)

@app.route("/prediction/<home>/<away>")
def make_predict(home,away):
    prediction = model_predict(home,away)
    return jsonify(prediction)


    











if __name__ == "__main__":
    app.run(debug=True)

