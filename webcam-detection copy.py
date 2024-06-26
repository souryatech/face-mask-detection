import cv2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import tensorflow as tf
import os
import numpy as np
import json

from mtcnn import MTCNN

detector = MTCNN()





MODEL = tf.keras.models.load_model(os.path.join('models','Mask1'))
classes = ['Mask', 'No Mask']
cap = cv2.VideoCapture(0)
n = 0

def detect_frame(frame, mask_model, face_model):
    object = face_model.detect_faces(frame)
    [x,y,w,h] = object[0]['box']
    # print(x)
    # print(y)
    # print(w)
    # print(h)
    # cv2.rectangle(frame, (x, y), ((x+w), (y+h)), (0,255,0), 2)
    # json_data = json.loads(face_model.detect_faces(frame))
    # print(json_data['box'])
    # print(frame)
    # for i in range(2):

    #     frame[i] = frame[i][y:y+h][x:x+h]
    # print(frame.shape)
    # pred = None
    frame = frame[y:y+h,x:x+h]
    frame = tf.image.resize(frame,(256,256))
    pred = mask_model.predict(np.expand_dims(frame,0))

    return pred, x, y, w, h


while(True):
    # n += 1
    
    ret, frame = cap.read()
    
    # cv2.imshow('frame',frame)

    rgb_frame = frame[:, :, ::]

    pred, x, y, w, h = detect_frame(rgb_frame, MODEL, detector)
    print(classes[np.argmax(pred)])
    cv2.rectangle(rgb_frame, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow('frame', rgb_frame)
  

    # if (n%5) == 0:
        # new = tf.image.resize(rgb_frame,(256,256))
        # predict = MODEL.predict(np.expand_dims(new/255,0))
        # print(predict)
        # print(classes[np.argmax(predict)])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()