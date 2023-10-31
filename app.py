from flask import Flask
from flask_opencv_streamer.streamer import Streamer
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np
import base64
import requests
import json
import pandas as pd
from flask import request
from flask_cors import CORS
import h5py
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.storage.blob import BlobClient
from PIL import Image
import scipy
from uuid import uuid4 


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
    
    unique_filename = str(uuid4()) + ".png"
    image_path = os.path.join('image', unique_filename)
    cv2.imwrite(image_path, original_image)

    # Upload the saved image to blob storage
    connection_string = "DefaultEndpointsProtocol=https;AccountName=eyeguardml;AccountKey=jSk2MVdYzFSDJQV1IEmjvAE35ZerAHtMnZcUvPSuXPsxicVayoYlogLEJeCSEciJLELiyfhTfPvT+AStPgYBrQ==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_name = "uploadedimg"
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=unique_filename)

    with open(image_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    # Continue with your processing and predictions...

    os.remove(image_path)

    processed_image = processing(original_image)
    cv2.imwrite(os.path.join('image', 'temp_image.png'), processed_image*255.0, [cv2.IMWRITE_JPEG_QUALITY, 90])

    test = pd.DataFrame({
    'ID': ['temp_image.png'],
    'Disease_Risk': [0], 'DR': [0], 'ARMD': [0], 'MH': [0], 'DN': [0], 'MYA': [0], 'BRVO': [0], 'TSLN': [0],
    'ERM': [0], 'LS': [0], 'MS': [0], 'CSR': [0], 'ODC': [0], 'CRVO': [0], 'TV': [0], 'AH': [0], 'ODP': [0],
    'ODE': [0], 'ST': [0], 'AION': [0], 'PT': [0], 'RT': [0], 'RS': [0], 'CRS': [0], 'EDN': [0], 'RPEC': [0],
    'MHL': [0], 'RP': [0], 'CWS': [0], 'CB': [0], 'ODPM': [0], 'PRH': [0], 'MNF': [0], 'HR': [0], 'CRAO': [0],
    'TD': [0], 'CME': [0], 'PTCR': [0], 'CF': [0], 'VH': [0], 'MCA': [0], 'VS': [0], 'BRAO': [0], 'PLQ': [0],
    'HPED': [0], 'CL': [0]
    })
    dataset_path = 'image'
    target_size = 224
    batch_size = 1
    datagen = ImageDataGenerator(rescale=1.0 / 255.0)

    test_data_generator = datagen.flow_from_dataframe(
        dataframe=test,
        directory=dataset_path,
        x_col='ID',
        y_col=test.columns[1:],
        target_size=(target_size, target_size),
        batch_size=batch_size,
        class_mode='other',
        shuffle=False
    )

    prediction_label, prediction_probability = predict(test_data_generator)

    prediction_label = int(prediction_label[0])
    prediction_probability = float(prediction_probability[0])
    
    if prediction_label == 1:
        result_text = f"We're sorry you may have cancer with a probability of {round(prediction_probability, 2)}%"
    else:
        result_text = f"Congratulaions! You don't have cancer with a probability of {round(100 - prediction_probability, 2)}%"

    os.remove(os.path.join('image', 'temp_image.png'))

    return result_text


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
    
    image_array = np.array(output_image)
    image_array = image_array / 255.0
    mean = np.array([0.485, 0.456, 0.406])
    image_array = image_array - mean
    std = np.array([0.229, 0.224, 0.225])
    image_array = image_array / std
    
    return image_array


def load_model_from_url(model_url):
    # download model from url
    response = requests.get(model_url)
    with open("model.h5", "wb") as model_file:
        model_file.write(response.content)


# url to model stored in azure blob storage
# available until november 4th 2023
model_url = "https://eyeguardml.blob.core.windows.net/model/datacamp_model.h5?sp=ra&st=2023-10-30T14:38:12Z&se=2023-11-04T22:38:12Z&sv=2022-11-02&sr=b&sig=D58asX3FDwNNVRSWLoo7DLlH9kQFRpoD8L7JJEZN598%3D"
load_model_from_url(model_url)


def predict(image):
    model = keras.models.load_model("model.h5")
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