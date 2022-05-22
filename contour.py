# Sami Muduroglu

import cv2 as cv

img = cv.imread('Media/dog.jpeg')

cv.imshow('Dog', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Using Canny and Blur

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

contour = cv.Canny(blur, 125, 175)

cv.imshow('Edges', contour)

# Using threshold

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(str(len(contours)) + ' contours found')

cv.waitKey(0)