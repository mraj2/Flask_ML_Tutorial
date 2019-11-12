from flask import Flask, render_template, request
from werkzeug import secure_filename

from keras.models import Sequential
from keras.models import model_from_json

import sys
sys.path.append("/home/muruganr/Documents/Tutorial/Flask/Dog-Cat-Classifier")
from get_dataset import get_img
import numpy as np

app = Flask(__name__)

# /home/muruganr/Documents/Tutorial/Flask/Dog-Cat-Classifier/Data/Model

class Dog_Cat_Classifier():
    def __init__(self):
        # Getting model:
        self.model_file = open('Dog-Cat-Classifier/Data/Model/model.json', 'r')
        self.model = self.model_file.read()
        self.model_file.close()
        self.model = model_from_json(self.model)
        # Getting weights
        self.model.load_weights("Dog-Cat-Classifier/Data/Model/weights.h5")
        self.model._make_predict_function()

    def image_preprocess(self, img_dir):
        img = get_img(img_dir)
        X = np.zeros((1, 64, 64, 3), dtype='float64')
        X[0] = img
        return X

    def predict_res(self, img):
        Y = np.argmax(self.model.predict(img), axis=1)
        result = 'cat' if Y[0] == 0 else 'dog'
        return result

DCC = Dog_Cat_Classifier()

@app.route('/')
def index():
   return render_template('Dog-Cat-Classifier.html')
	
@app.route('/predict_cat_dog', methods = ['GET', 'POST'])
def upload_file():
    global DCC

    if request.method == 'POST':
        f = request.files['file']
        
        f_name = secure_filename(f.filename)
        f.save(f_name)

        img = DCC.image_preprocess(f_name)
        result = DCC.predict_res(img)  
        
        print(f'Image predicted as: {result}')      

        return f'Image predicted as: {result}'


if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = "5000", debug=True)