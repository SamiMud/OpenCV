# Sami Muduroglu

import cv2 as cv

# Resizing an Image or existing video

img = cv.imread('dog.jpeg')

def rescaleFrame(frame, scale=0.75):

    width = int(frame.shape[1] * scale)
    width = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



# Resizing a LIVE video
capture = cv.VideoCapture('dog.mp4')

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

