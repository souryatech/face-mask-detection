import cv2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import tensorflow as tf
import os
import numpy as np

MODEL = tf.keras.models.load_model(os.path.join('models','Mask1'))
classes = ['No Mask', 'Mask']
cap = cv2.VideoCapture(0)
n = 0

def detect_frame(frame, mask_model, face_model):
    preprocess_input()
while(True):
    n += 1
    
    ret, frame = cap.read()
    
    cv2.imshow('frame',frame)
    if (n%30) == 0:
        new = tf.image.resize(frame,(256,256))
        predict = MODEL.predict(np.expand_dims(new/255,0))
        print(predict)
        print(classes[np.argmax(predict)])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()