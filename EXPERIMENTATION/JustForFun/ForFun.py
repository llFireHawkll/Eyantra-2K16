# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task1C
*  Filename: getCellVal.py
*  Version: 1.0.0  
*  Date: October 13, 2016
*  
*  Author: Jayant Solanki, e-Yantra Project, Department of Computer Science
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
"""
import cv2
import numpy as np

frame =cv2.imread('6.jpg')
template =cv2.imread('image.jpg',0)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,130,255,cv2.THRESH_TOZERO)



hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
lower_red = np.array([10,20,20])
upper_red = np.array([255,255,255])
    
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_or(frame,frame, mask= mask)

cv2.imshow('Original',frame)
edges = cv2.Canny(thresh1,200,300)
cv2.imshow('Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

