import cv2
import numpy as np


# Reading Image
img = cv2.imread("19.jpg")
cv2.namedWindow("Original Image",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Original Image",img)
# Display image

# RGB to Gray scale conversion
img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.namedWindow("Gray Converted Image",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Gray Converted Image",img_gray)
# Display Image

# Noise removal with iterative bilateral filter(removes noise while preserving edges)
noise_removal = cv2.bilateralFilter(img_gray,9,75,75)
cv2.namedWindow("Noise Removed Image",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Noise Removed Image",noise_removal)
# Display Image

# Histogram equalisation for better results
equal_histogram = cv2.equalizeHist(img_gray)
cv2.namedWindow("After Histogram equalisation",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("After Histogram equalisation",equal_histogram)
# Display Image

# Morphological opening with a rectangular structure element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
morph_image = cv2.morphologyEx(img_gray,cv2.MORPH_OPEN,kernel,iterations=25)
cv2.namedWindow("Morphological opening",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Morphological opening",morph_image)
# Display Image

# Image subtraction(Subtracting the Morphed image from the histogram equalised Image)
sub_morp_image = cv2.subtract(equal_histogram,morph_image)
cv2.namedWindow("Subtraction image", cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Subtraction image", sub_morp_image)
# Display Image

# Thresholding the image
ret,thresh_image = cv2.threshold(sub_morp_image,127,255,cv2.THRESH_OTSU)
cv2.namedWindow("Image after Thresholding",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Image after Thresholding",thresh_image)
# Display Image

# Applying Canny Edge detection
canny_image = cv2.Canny(thresh_image,250,255)
cv2.namedWindow("Image after applying Canny",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Image after applying Canny",canny_image)
# Display Image
canny_image = cv2.convertScaleAbs(canny_image)

# dilation to strengthen the edges
kernel = np.ones((3,3), np.uint8)
# Creating the kernel for dilation
dilated_image = cv2.dilate(canny_image,kernel,iterations=1)
cv2.namedWindow("Dilation", cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Dilation", dilated_image)
# Displaying Image

cv2.waitKey() # Wait for a keystroke from the user
