# -*- coding: utf-8 -*-
'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2014)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Functions
*  Filename: contourImage.py
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

import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt

def nothing(*arg):
        pass

cv2.namedWindow('COLOR')
cv2.createTrackbar('THRESH-1', 'COLOR', 0, 255, nothing)
cv2.createTrackbar('THRESH-2', 'COLOR', 0, 255, nothing)
cv2.createTrackbar('THRESH-3', 'COLOR', 0, 255, nothing)
cv2.createTrackbar('THRESH-4', 'COLOR', 0, 255, nothing)
cv2.createTrackbar('THRESH-5', 'COLOR', 0, 255, nothing)
cv2.createTrackbar('M1', 'COLOR', 1, 10, nothing)
cv2.createTrackbar('M2', 'COLOR', 1, 10, nothing)

img = cv2.imread('19.jpg')
template = cv2.imread('Digits_1/8.jpg',0)
w, h = template.shape[::-1]
img2 = img.copy()
output = img.copy()


############################# testing part  #########################
out = np.zeros(img.shape,np.uint8)

while True:
    
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #gray1 = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
        
        th1 = cv2.getTrackbarPos('THRESH-1', 'COLOR')
        th2 = cv2.getTrackbarPos('THRESH-2', 'COLOR')
        th3 = cv2.getTrackbarPos('THRESH-3', 'COLOR')
        th4 = cv2.getTrackbarPos('THRESH-4', 'COLOR')
        th5 = cv2.getTrackbarPos('THRESH-5', 'COLOR')

        M1 = cv2.getTrackbarPos('M1', 'COLOR')
        M2 = cv2.getTrackbarPos('M2', 'COLOR')
 
        ret,thresh1 = cv2.threshold(gray,th1,255,cv2.THRESH_BINARY)
        #ret,thresh1_1 = cv2.threshold(template,th1,255,cv2.THRESH_BINARY)
        
        ret,thresh2 = cv2.threshold(gray,th2,255,cv2.THRESH_BINARY_INV)
        ret,thresh3 = cv2.threshold(gray,th3,255,cv2.THRESH_TRUNC)
        ret,thresh4 = cv2.threshold(gray,th4,255,cv2.THRESH_TOZERO)
        ret,thresh5 = cv2.threshold(gray,th5,255,cv2.THRESH_TOZERO_INV)

        #cv2.imshow('ORIGINAL IMAGE',img1)
        #%cv2.imshow('THRESH-1',thresh1)
        #cv2.imshow('THRESH-2',thresh2)
        #cv2.imshow('THRESH-3',thresh3)
        #cv2.imshow('THRESH-4',thresh4)
        #cv2.imshow('THRESH-5',thresh5)


        
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (M1,M2))

        erosion = cv2.erode(thresh4,kernel,iterations = 1)
       # erosion_1 = cv2.erode(thresh1_1,kernel,iterations = 1)
        
        dilation = cv2.dilate(thresh4, kernel, iterations = 1)
       # dilation_1 = cv2.dilate(thresh1_1, kernel, iterations = 1)
        

        opening = cv2.dilate(erosion, kernel, iterations = 1)
       # opening_1 = cv2.dilate(erosion_1, kernel, iterations = 1)
        
        closing = cv2.erode(dilation, kernel, iterations = 1)
       # closing_1 = cv2.erode(dilation_1, kernel, iterations = 1)
        
        gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
       # gradient_1 = cv2.morphologyEx(template, cv2.MORPH_GRADIENT, kernel)
         
        cv2.imshow('erosion', erosion)
        cv2.imshow('dilation', dilation)
        cv2.imshow('opening', opening)
        cv2.imshow('closing', closing)
       
        
        #cv2.imshow('erosion_1', erosion_1)
        #cv2.imshow('dilation_1', dilation_1)
        #cv2.imshow('opening_1', opening_1)
        #cv2.imshow('closing_1', closing_1)
     

        img2 = cv2.subtract(dilation-opening,gray)
        cv2.imshow('subtract', img2)
        
        res = cv2.matchTemplate(erosion,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.imshow('res.png',img)

        
        """ 
        circles = cv2.HoughCircles(thresh1,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=1,maxRadius=4)
 
        # ensure at least some circles were found
        if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
                circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
                for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
                        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
	# show the output image
                cv2.imshow("output", np.hstack([img, output]))
        """
        ch = cv2.waitKey(5)
        if ch == 27:
            break
cv2.destroyAllWindows()















