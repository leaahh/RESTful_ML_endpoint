from pyexpat import model
from tensorflow import keras 
import numpy as np
import model as md 


def load_model():
  """
  # Charging the model in memory 
  """
  return keras.models.load_model("model.h5")

model = load_model()  

def parse_img(p_img_pixels) :
  return np.array([np.fromstring(p_img_pixels.replace("[","").replace("]","").replace("\n","").replace(" ",""), sep=",").reshape(28,28)])

def get_class(p_input):
  image = parse_img(p_input)
  y_pred = model.predict(image)
  return md.class_names[np.argmax(y_pred[0])]