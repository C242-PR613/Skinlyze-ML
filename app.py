# using flask_restful 
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
import os
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
import urllib.request

  
# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 

def predict(img_url):
  model = tf.keras.models.load_model("model/model.h5", compile=False)
  req = urllib.request.urlretrieve(img_url)
  class_disease = ['akiec', 'bcc', 'bkl', 'df', 'mel','nv', 'vasc']
      # {'ISIC_0034524':'nv', 'ISIC_0034525':'nv', 'ISIC_0034526':'bkl'}
  def load(filename):
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = tf.image.resize(np_image, (28,28))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image

  image = load(req[0])
  print(image.shape)
  res = model.predict(image)
  print(res)
  print(res.max())
  print(class_disease[res.argmax()])
  data = {'message':'success','data':{"prediction":res.tolist(), "result":class_disease[res.argmax()],"score":res.max().item()}}
  return data
  
# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
class Model(Resource): 
  
    # corresponds to the GET request. 
    # this function is called whenever there 
    # is a GET request for this resource 
    def get(self): 
      # Recreate the exact same model, including its weights and the optimizer
      image_url = "https://storage.googleapis.com/skinlyze-image-scan/ISIC_0034526.jpg"
      res = predict(image_url)
      return res, 200
  
    # Corresponds to POST request 
    def post(self):   
        args = request.get_json()
        image_url = args["image_url"]
        res = predict(image_url)
        return res, 200
  
# adding the defined resources along with their corresponding urls 
api.add_resource(Model, '/predict') 
  
# driver function 
if __name__ == '__main__': 
    app.run(port=8080,host="0.0.0.0") 