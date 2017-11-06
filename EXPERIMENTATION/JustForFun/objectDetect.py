# -*- coding: utf-8 -*-
'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2014)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Functions
*  Filename: objectDetect.py
*  Version: 1.0.0  
*  Date: November 3, 2014
*  
*  Author: Arun Mukundan, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
'''
#img1 = img[390:480, 170:450]
############################################
## Import OpenCV
import numpy as np
import cv2
import sys

def nothing(*arg):
        pass

cv2.namedWindow('COLOR')
cv2.createTrackbar('LOWER_H', 'COLOR', 0, 179, nothing)
cv2.createTrackbar('UPPER_H', 'COLOR', 0, 179, nothing)
cv2.createTrackbar('LOWER_S', 'COLOR', 0, 255, nothing)
cv2.createTrackbar('UPPER_S', 'COLOR', 0, 255, nothing)
cv2.createTrackbar('LOWER_V', 'COLOR', 0, 255, nothing)
cv2.createTrackbar('UPPER_V', 'COLOR', 0, 255, nothing)

img = cv2.imread('output_image.jpg')
h, w, channels = img.shape
img1 = img[h/2:, :w]

cv2.imshow('image1',img)


while True:
    
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        LH = cv2.getTrackbarPos('LOWER_H', 'COLOR')
        UH = cv2.getTrackbarPos('UPPER_H', 'COLOR')
        LS = cv2.getTrackbarPos('LOWER_S', 'COLOR')
        US = cv2.getTrackbarPos('UPPER_S', 'COLOR')
        LV = cv2.getTrackbarPos('LOWER_V', 'COLOR')
        UV = cv2.getTrackbarPos('UPPER_V', 'COLOR')

        lower = np.array([LH,LS,LS])
        upper = np.array([UH,US,US])
        mask  = cv2.inRange(hsv, lower, upper)
        res   = cv2.bitwise_and(img, img, mask= mask)
        #cv2.imshow('image1',img)
        cv2.imshow('image',hsv)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)

        ch = cv2.waitKey(5)
        if ch == 27:
            break
cv2.destroyAllWindows()

