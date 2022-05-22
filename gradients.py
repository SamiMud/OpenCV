# Sami Muduroglu
import cv2 as cv
import numpy as np

img = cv.imread('Media/dog.jpeg')
cv.imshow('Dog', img)

gray = cv.cvtColor(img, cv.COLqOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

# Combine x and y sobels
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combinel Sobel', combined_sobel) 

# Canny

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)