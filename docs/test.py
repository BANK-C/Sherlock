import cv2
import time
import uuid
import os

camera = cv2.VideoCapture(0)
int1 = 0
while(True):
    _, image = camera.read()
<<<<<<< HEAD
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    crop_w = int(width/3)
    crop_w2 = int(width* 2/3)
    cropped = image[0:height, crop_w:crop_w2]
=======
    #cropped = image[0:720, 440:840]
    cropped= image
>>>>>>> 887c37daa8d559d477dec342792bd26e22c24628
    cv2.imwrite("test"+'.png', cropped)
    time.sleep(5)
    os.system('python woohoo.py')
