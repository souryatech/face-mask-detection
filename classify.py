import tensorflow as tf
import os
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt


MODEL = load_model(os.path.join('models','Mask1'))


from keras.preprocessing import image

img = 'image.png'


classes = ['Wearing Mask','Not Wearing Mask']


test_image = image.load_img(img)



test_image = image.img_to_array(test_image)

test_image = tf.image.resize(test_image,(256,256))

predict = MODEL.predict(np.expand_dims(test_image,0))

print(classes[np.argmax(predict)])
print(f"Confidence: {np.max(predict)}")