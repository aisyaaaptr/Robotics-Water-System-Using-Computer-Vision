from collections import deque
import serial
import numpy as np
import argparse
import imutils
import cv2
import string
import os
import math
import datetime
import time
from imutils.video import WebcamVideoStream

arduino = serial.Serial('COM11',115200)

################################################################################
##Camera Parameter 
im_widht=600
im_height=450
center_im=im_widht/2,im_height/2
camera = cv2.VideoCapture(0)


#Nilainya sama dengan HSV
Hmin = 42
Hmax = 88
Smin = 62
Smax = 255
Vmin = 45
Vmax = 150
out1 = 0


while (1):
  
        stream = cv2.waitKey(1)
        (grabbed,frame) = camera.read()
        frame = imutils.resize(frame, width=im_widht)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        Lower_val = np.array([Hmin,Smin,Vmin])
        Upper_val = np.array([Hmax,Smax,Vmax])
        mask = cv2.inRange(hsv, Lower_val, Upper_val)
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = 1
        cnts= cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = 1
        try :
                if len(contours) > 0:
                    cntr = max(contours, key=cv2.contourArea)
                    ((x, y), radius) = cv2.minEnclosingCircle(cntr)
                    hull = cv2.convexHull(cntr)
                    M = cv2.moments(cntr)
                    #center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    
                    center_x = int(M["m10"] / M["m00"])
                    center_y = int(M["m01"] / M["m00"])
                    cv2.drawContours(frame, [hull], 0, (0,255,255) ,2)
                    mask = np.zeros(frame.shape[:2], np.uint8)
                    cv2.drawContours(frame, [hull], 0, (0,255,255) ,2)
                    cv2.rectangle(frame, (int(x) - 3, int(y) - 3), (int(x) + 3, int(y) + 3), (0, 0, 255), -1)
                    if(center_x >=1 and center_x < 200) and (center_y >1 and center_y < 150):
                       out1 = 'A'
                       print('A')
                       #arduino.write(out1)
                    elif(center_x > 200 and center_x < 400) and (center_y >1 and center_y < 150):
                       out1 = 'B'
                       print('B')
                       #arduino.write(out2)
                    elif(center_x > 400 and center_x < 1200) and (center_y >1 and center_y < 150):
                       out1 = 'C'
                       print('C')
                       #arduino.write(out3)
                    elif(center_x >= 1  and center_x < 200) and (center_y >150 and center_y < 300):
                       out1 = 'D'
                       print('D')
                       #arduino.write(out4)
                    elif(center_x > 200 and center_x < 400) and (center_y >150 and center_y < 300):
                       out1 = 'E'
                       print('E')
                       #arduino.write(out5)
                    elif(center_x > 400 and center_x < 1200) and (center_y >150 and center_y < 300):
                       out1 = 'F'
                       print('F')
                       #arduino.write(out6)
                    elif(center_x >= 1  and center_x < 200) and (center_y >300 and center_y < 1200):
                       out1 = 'G'
                       print('G')
                       #arduino.write(out7)
                    elif(center_x > 200 and center_x < 400) and (center_y >300 and center_y < 1200):
                       out1 = 'H'
                       print('H')
                       #arduino.write(out8)
                    elif(center_x > 400 and center_x < 1200) and (center_y >300 and center_y < 1200):
                       out1 = 'J'
                       print('J')
                       #arduino.write(out9)
                    
                    else:
                        pass
                    arduino.write(out1.encode())

                else:
                        pass
        except :
                pass
        cv2.line(img=frame, pt1=(0, 300), pt2=(4000, 300), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
        cv2.line(img=frame, pt1=(0, 600), pt2=(4000, 600), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
        cv2.line(img=frame, pt1=(400, 0), pt2=(400, 4500), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
        cv2.line(img=frame, pt1=(850, 0), pt2=(850, 4500), color=(0, 255, 0), thickness=2, lineType=8, shift=1)
        img = imutils.resize(frame, width=800)
        cv2.imshow('image',img)
        '''
        try:
            arduino = serial.Serial("com8", 9600)
            arduino.isOpen()
        except serial.serialutil.SerialException:
            arduino = None
        else:
            if arduino.is_open:
                arduino.write(out1)
                time.sleep(0.054)
            else:
                print("Serial port is not open.")
        '''
        #print("Tengah", center)
        if stream & 0XFF == ord('q'):  #Letter 'q' is the escape key
                print("Video Berakhir")
                break 
camera.release()
cv2.destroyAllWindows()
print("Selesai")
