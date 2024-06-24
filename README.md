## **Face Mask Classification**

 - Takes the input of an image & returns classification whether person in the image is wearing a face mask or not
 - 95% accuracy, requires a normal or better quality camera for better performance

**Use Cases**
- Can be utilized to prevent disease spread in certain places
- Can also be utilized to enforce certain regulations in specific areas
- Can also be a fascinating tool to utilize 

**How To Use**
- First clone the repository and download it on your computer
- A python file can then be made in the same directory and import **tensorflow as tf**, **numpy as np**, **cv2**, **os** & **matplotlib.pyplot as plt** (if you want to display the picture)
- Then type in `model = tf.keras.models.load_model(os.path.join('models','Mask1'))`
- Then drag and drop the image you want to classify on the directory
- You can then use `yhat = model.predict(np.expand_dims(cv2.imread(os.path.join('image.filetype')),0)` and then `print(yhat)` to see which of the two classes has higher probability: [mask, non mask]
- The class that has higher probability is the class that the model predicts
- A website/app that can take in camera input by frame will eventually be made


 - Credit to Kaggle dataset: https://www.kaggle.com/datasets/prithwirajmitra/covid-face-mask-detection-dataset