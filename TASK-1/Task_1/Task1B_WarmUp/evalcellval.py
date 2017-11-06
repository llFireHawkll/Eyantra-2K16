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

def detectCellVal(img_rgb,grid_map):
    for i in range(0,6):
        for j in range(0,6):
            img1 = img_rgb[(i*100):((i*100)+100), (j*100):((j*100)+100)]
            gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
            ret1,thresh1 = cv2.threshold(gray1,127,255,0)
            contours1, hierarchy1 = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            if(len(contours1) == 1):
                grid_map[i][j] == 0
            else :
                cnt1 = contours1[1]

                for k in range(0,10):
                    img2 = cv2.imread('digits/'+str(k)+'.jpg')
                    gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
                    ret2,thresh2 = cv2.threshold(gray2,127,255,0)
                    contours2, hierarchy2 = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

                    cnt2 = contours2[1]
                    
                    ret2 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)

                    if(ret2 == 0.0):
                        grid_map[i][j] = k
                        break
                
                img2 = cv2.imread('digits/plus.jpg')
                gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
                ret2,thresh2 = cv2.threshold(gray2,127,255,0)
                contours2, hierarchy2 = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

                cnt2 = contours2[1]
                    
                ret2 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)

                if(ret2 == 0.0):
                    grid_map[i][j] = '+'
                    

                img2 = cv2.imread('digits/minus.jpg')
                gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
                ret2,thresh2 = cv2.threshold(gray2,127,255,0)
                contours2, hierarchy2 = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

                cnt2 = contours2[1]
                    
                ret2 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)

                if(ret2 == 0.0):
                    grid_map[i][j] = '-'    
                          
    return grid_map
