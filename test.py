import cv2
import time
import uuid
import os

camera = cv2.VideoCapture(0)
int1 = 0
while(True):
    _, image = camera.read()
    cv2.imwrite("test"+'.png', image)
    time.sleep(5)
    os.system('python woohoo.py')