import cv2
import time
import uuid
import os

camera = cv2.VideoCapture(0)
int1 = 0
while(True):
    _, image = camera.read()

    #cropping
    #print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    crop_w = int(width/3)
    crop_w2 = int(width* 2/3)
    cropped = image[0:height, crop_w:crop_w2]



    #cv2.imwrite("test.png", cropped)
    cv2.imwrite("test.png", image)
    time.sleep(5)
    os.system('python3 woohoo.py')
