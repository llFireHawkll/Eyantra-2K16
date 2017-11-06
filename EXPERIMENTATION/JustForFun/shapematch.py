# -*- coding: utf-8 -*-
import numpy as np
import cv2
import sys

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
img7 = cv2.imread('1.3.jpg')

############################# testing part  #########################


while True:
    
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray1 = cv2.cvtColor(img7,cv2.COLOR_BGR2GRAY)
        
        th1 = cv2.getTrackbarPos('THRESH-1', 'COLOR')
        th2 = cv2.getTrackbarPos('THRESH-2', 'COLOR')
        th3 = cv2.getTrackbarPos('THRESH-3', 'COLOR')
        th4 = cv2.getTrackbarPos('THRESH-4', 'COLOR')
        th5 = cv2.getTrackbarPos('THRESH-5', 'COLOR')

        M1 = cv2.getTrackbarPos('M1', 'COLOR')
        M2 = cv2.getTrackbarPos('M2', 'COLOR')
 
        ret,thresh1 = cv2.threshold(gray,th1,255,cv2.THRESH_BINARY)
        ret,thresh1_1 = cv2.threshold(gray1,th1,255,cv2.THRESH_BINARY)
        
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

        erosion = cv2.erode(thresh1,kernel,iterations = 1)
        erosion_1 = cv2.erode(thresh1_1,kernel,iterations = 1)
        
        dilation = cv2.dilate(thresh1, kernel, iterations = 1)
        dilation_1 = cv2.dilate(thresh1_1, kernel, iterations = 1)
        

        opening = cv2.dilate(erosion, kernel, iterations = 1)
        opening_1 = cv2.dilate(erosion_1, kernel, iterations = 1)
        
        closing = cv2.erode(dilation, kernel, iterations = 1)
        closing_1 = cv2.erode(dilation_1, kernel, iterations = 1)
        
       # gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
       # gradient_1 = cv2.morphologyEx(template, cv2.MORPH_GRADIENT, kernel)
         
        #cv2.imshow('erosion', erosion)
        #cv2.imshow('dilation', dilation)
        #cv2.imshow('opening', opening)
        #cv2.imshow('closing', closing)
       
        
        #cv2.imshow('erosion_1', erosion_1)
        #cv2.imshow('dilation_1', dilation_1)
        #cv2.imshow('opening_1', opening_1)
        #cv2.imshow('closing_1', closing_1)
     


        """res = cv2.matchTemplate(erosion,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.imshow('res.png',img)

        """
        
        """
        contours, heirs = cv2.findContours( thresh5.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt)>50:
                [x,y,w,h] = cv2.boundingRect(cnt)
                if  h>28:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                    roi = thresh5[y:y+h,x:x+w]
                    roismall = cv2.resize(roi,(10,10))
                    roismall = roismall.reshape((1,100))
                    roismall = np.float32(roismall)
                    retval, results, neigh_resp, dists = model.find_nearest(roismall, k = 1)
                    string = str(int((results[0][0])))
                    cv2.putText(out,string,(x,y+h),0,1,(0,255,0))

        cv2.imshow('im',img)
        cv2.imshow('out',out)
        """

        contours,hierarchy = cv2.findContours(erosion,2,1)
        contours1,hierarchy = cv2.findContours(gray1,2,1)
        print len(contours1)
        cv2.drawContours(img7,contours1,-1,(0,255,0),3)
        cv2.imshow('contours', img7)
        #ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
        #print ret

       
        ch = cv2.waitKey(5)
        if ch == 27:
            break
cv2.destroyAllWindows()
