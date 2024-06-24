import tensorflow as tf
import os
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import cv2

def read_img(image):
    img_array = cv2.imread(image)

    return img_array


classes = ['Wearing Mask','Not Wearing Mask']

img_dir = 'image.filetype'

img = read_img(img_dir)
img = tf.image.resize(img,(256,256))

# plt.imshow(img)
MODEL = load_model(os.path.join('models','Mask1'))


yhat = MODEL.predict(np.expand_dims((img),0))
print(classes[np.argmax(yhat[0])])
print(f'Confidence: {np.max(yhat[0])}')