import cv2
import tensorflow as tf
import os
import numpy as np
import json

from mtcnn import MTCNN

detector = MTCNN()





MODEL = tf.keras.models.load_model(os.path.join('models','Mask1'))
classes = ['No Mask', 'Mask']
cap = cv2.VideoCapture(0)
n = 0

def detect_frame(frame, mask_model, face_model):
    object = face_model.detect_faces(frame)
    [x,y,w,h] = object[0]['box']
  
    frame = frame[y:y+h,x:x+h]
    frame = cv2.resize(frame, (256,256))
    # frame = tf.image.resize(frame,(256,256))
    pred = mask_model.predict(np.expand_dims(frame,0))

    return pred, x, y, w, h


while(True):
    # n += 1
    
    ret, frame = cap.read()
    

    rgb_frame = frame[:, :, ::]

    pred, x, y, w, h = detect_frame(rgb_frame, MODEL, detector)
    print(classes[np.argmax(pred)])
    color = (0,0,0)
    if np.argmax(pred) == 0:
        color = (255,0,0)
    elif np.argmax(pred) == 1:
        color = (0,0,255)

    cv2.putText(rgb_frame, classes[np.argmax(pred)],(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,0.5,color,2,cv2.LINE_AA)
    cv2.rectangle(rgb_frame, (x,y), (x+w, y+h), color, 3)
    cv2.imshow('frame', rgb_frame)
  

  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()