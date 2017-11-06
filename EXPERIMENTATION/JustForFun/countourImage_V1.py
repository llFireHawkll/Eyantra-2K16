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

############################################
## Import OpenCV
import numpy
import cv2
from matplotlib import pyplot as plt
############################################

############################################
## Read the image
img = cv2.imread('19.2.jpg')
img1 = img[390:480, 170:200]
img2 = img[390:480, 420:450]
############################################
h, w, channels = img.shape

print img.shape
img1 = img[h/2:, :w]



############################################
############################################
## Do the processing
# Need a binary Image
i = -1
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,130,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(gray,135,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(gray,135,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(gray,135,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(gray,135,255,cv2.THRESH_TOZERO_INV)

contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img1,contours,-1,(0,255,0),3)
print len(contours)



############################################

############################################
## Show the image
cv2.imshow('image',img1)
#cv2.imshow('image1',res1)
#cv2.imshow('image2',gray)

#cv2.imshow('image - thresh1',thresh1)
#cv2.imshow('image - thresh3',thresh3)
#cv2.imshow('image - thresh4',thresh4)
#cv2.imshow('image - thresh5',thresh5)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
