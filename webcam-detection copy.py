import cv2
import tensorflow as tf
import os
import numpy as np

from mtcnn import MTCNN

from imutils.video import VideoStream

detector = MTCNN()





MODEL = tf.keras.models.load_model(os.path.join('models','Mask1'))
classes = ['No Mask', 'Mask']
# cap = cv2.VideoCapture(0)
vs = VideoStream(src=0).start()
n = 0

def detect_frame(frame, mask_model, object, i):
    
    [x,y,w,h] = object[i]['box']
    if not any([x,y,w,h]):
        return False, False, False, False, False
  
    frame = frame[y-10:y+h+10,x-10:x+h+10]
    frame = cv2.resize(frame, (256,256))
    # frame = tf.image.resize(frame,(256,256))
    pred = mask_model.predict(np.expand_dims(frame,0))

    return pred, x, y, w, h


while(True):
    # n += 1
    
    frame = vs.read()    

    rgb_frame = frame[:, :, ::]
    object = detector.detect_faces(frame)
    for i in range(len(object)):
        pred, x, y, w, h = detect_frame(rgb_frame, MODEL, object, i)
    
        color = (0,0,0)
        if x:

            if np.argmax(pred) == 0:
                color = (255,0,0)
            elif np.argmax(pred) == 1:
                color = (0,0,255)

            cv2.putText(rgb_frame, classes[np.argmax(pred)],(x-10,y+h-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,color,2,cv2.LINE_AA)
            cv2.rectangle(rgb_frame, (x-10,y-10), (x+w+10, y+h+10), color, 3)
    cv2.imshow('frame', rgb_frame)
  

  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
vs.stop()