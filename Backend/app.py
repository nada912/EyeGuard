from flask import Flask
from flask_opencv_streamer.streamer import Streamer
from tensorflow import keras
from keras.models import load_model
import cv2
import numpy as np
import base64
import requests
import json
from flask import request
from flask_cors import CORS


app = Flask(__name__)

CORS(app, ressources = {r"/*":{'origins' : 'http://http://localhost:8081', "allow_headers" : "Acces-Control-Allow-Origin"}})

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/getresults/', methods = ['POST'])
def getimageandsendpreds():
    image = request.files['image']
    image_data = image.read()

    nparr = np.fromstring(image_data, np.uint8)

    original_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if original_image.shape[2] == 1:
        original_image = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)

    prediction_label, prediction_probability = predict(original_image)

    prediction_label = int(prediction_label[0])
    prediction_probability = float(prediction_probability[0])

    results = {
        'label': prediction_label,
        'probability': prediction_probability
    }

    results_json = json.dumps(results)

    return results_json, 200, {'Content-Type': 'application/json'}




def processing(image):
    target_size = 224

    height_scale = target_size / image.shape[0]
    width_scale = target_size / image.shape[1]

    scale_factor = min(height_scale, width_scale)

    resized_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

    padding_height = target_size - resized_image.shape[0]
    padding_width = target_size - resized_image.shape[1]

    output_image = np.zeros((target_size, target_size, 3), dtype=np.uint8)

    x_offset = padding_width // 2
    y_offset = padding_height // 2

    output_image[y_offset:y_offset + resized_image.shape[0], x_offset:x_offset + resized_image.shape[1]] = resized_image
    output_image = np.expand_dims(output_image, axis=0)

    return output_image

def predict(data):
    model = load_model("datacamp_model.h5")
    image = processing(data)
    predictions = model.predict(image)
    predicted_labels = (predictions > 0.5).astype(int)
    prediction_probabilitie_percentage = predictions * 100
    return (predicted_labels[0],prediction_probabilitie_percentage[0])


def get_predictions(data):
    data_list = data.tolist()
    
    image = {
        "image": data_list
    }
    
    headers = {'Content-Type': 'application/json'}

    response = requests.post('https://datacamp-model-osmdm.francecentral.inference.ml.azure.com/score', json=image, headers=headers)

    predictions = response.json()

    return predictions

