## **Face Mask Classification & Detection**

 - Takes the input of an image & returns classification whether person in the image is wearing a face mask or not
 - 95% accuracy, requires a normal or better quality camera for better performance

**Use Cases**
- Can be utilized to prevent disease spread in certain places
- Can also be utilized to enforce certain regulations in specific areas
- Can also be a fascinating tool to utilize 

**How To Use**
- First copy and paste this in your terminal:
 ```shell script
git clone https://github.com/souryatech/face-mask-detection.git
cd face-mask-detection
pip install -r requirements.txt
```
- You can classify an image or detect face masks from your web cam
- **Classify:**
 - First open https://github.com/souryatech/face-mask-detection/blob/0bde7701c2109f9d31b4ffc3a04775e14f523ef2/classify.py
 - Drag and drop the image file you want to classify onto the main directory
 - Copy the image file's name from the directory along with .filetype
 - Go to classify.py and replace the variable img with the text in quotes ('image.filetype' to '(name you copied).(image's filetype)')
 - Then run the file and a prediction will be outputted, Wearing Mask or Not Wearing Mask
- **Detect:**
 - Go to [webcam-detection.py](https://github.com/souryatech/face-mask-detection/blob/0bde7701c2109f9d31b4ffc3a04775e14f523ef2/webcam-detection.py)
 - Run the program
 - You can wear a mask and show up in the frame, it will place a bounding box over your face and classify whether you are wearing a mask or not
 - This program also can detect multiple faces and if they are wearing face masks
 - When a person takes off their mask, their box would be red and will indicate that they are not wearing a mask
  


 - Credit to Kaggle dataset: https://www.kaggle.com/datasets/prithwirajmitra/covid-face-mask-detection-dataset
