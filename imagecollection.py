import cv2
import os
import time
import uuid

IMAGE_PATH = "D:\Vscode\codes\PYTHON\python_projects\sign_language\RealTimeObjectDetection\Tensorflow\workspace\images\collectedimages"

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou'] 
number_imgs = 15
for label in labels:
    os.makedirs('D:\Vscode\codes\PYTHON\python_projects\sign_language\RealTimeObjectDetection\Tensorflow\workspace\images\collectedimages\\'+label)
    cap = cv2.VideoCapture(0)
    print('Collecting image for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret , frame = cap.read()
        imagename = os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame',frame)
        time.sleep(2)
        
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    cap.release()