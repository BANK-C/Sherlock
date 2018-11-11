import cv2
import time
import uuid
import os

camera = cv2.VideoCapture(0)
int1 = 0
while(True):
    _, image = camera.read()
    #cropped = image[0:720, 440:840]
    cropped= image
    cv2.imwrite("test"+'.png', cropped)
    time.sleep(5)
    os.system('python3 woohoo.py')
