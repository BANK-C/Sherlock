import cv2
import time
import uuid

camera = cv2.VideoCapture(0)
int1 = 0
while(True):
    _, image = camera.read()
    cv2.imwrite("test"+'.png', image)
    time.sleep(5)
