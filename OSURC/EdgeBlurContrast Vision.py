"""
NOTES OF IMPORTANCE:
You need opencv2, and numpy in order for this to work
This was written in python3.7
Experiment with the values to see what you can do

Thanks!
Graham Donaldson

Recommended Values:
Contrast: 1 to 10
Brightness: -30 to 30
Blur: 1-100, but it has to be an odd number
lowerThreshold: 80-130 ish
Threshold Ratio: 1-10 ish, haven't experimented much with this, go crazy!


PS: you need to have an image named "image.png" in the same directory as this script in order of the script to run. 
"""


import cv2, time
import numpy as np
import matplotlib.pyplot as plt

def contraster(img, alpha, beta):
    #alpha: contrast
    #beta: brightness
    contrasted_image = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)
    return contrasted_image

def blur(img, xDeviation, yDeviation):
    blur = cv2.GaussianBlur(img,(xDeviation,yDeviation),0)
    return blur

def edgeConverter(img, lowThreshold, thresRatio):
    edges = cv2.Canny(img, lowThreshold, lowThreshold*thresRatio)
    return edges

def nothing(x):
    pass

img = cv2.imread('image.png')
cv2.namedWindow('image')
cv2.createTrackbar('BLUR','image',0,100,nothing)
cv2.createTrackbar('CONTRAST','image',1,10,nothing)
cv2.createTrackbar('BRIGHTNESS','image',0,100,nothing)
cv2.createTrackbar('EDGE_Threshold','image',80,130,nothing)
cv2.createTrackbar('EDGE_Ratio','image',0,100,nothing)

while True:
    blurTrack = cv2.getTrackbarPos('BLUR','image')
    contrastTrack = cv2.getTrackbarPos('CONTRAST','image')
    brightnessTrack = cv2.getTrackbarPos('BRIGHTNESS', 'image')
    thresholdTrack = cv2.getTrackbarPos('EDGE_Threshold', 'image')
    ratioTrack = cv2.getTrackbarPos('EDGE_Ratio','image')
    if blurTrack == -1: #if the blur trackbar is in the starter value (-1)
        blurTrack = 1;
    elif blurTrack % 2 == 0: #if the trackbar is a even number
        blurTrack += 1;
    proccessedImage = edgeConverter(blur(contraster(img, contrastTrack, brightnessTrack), blurTrack, blurTrack),thresholdTrack, ratioTrack) #apply all filters
    proccessedImage = cv2.cvtColor(proccessedImage, cv2.COLOR_GRAY2RGB)
    shownImage = cv2.resize(np.hstack((img,proccessedImage)), (0,0), fx=0.7, fy=0.7)
    cv2.imshow('image',shownImage)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    
    
"""
#MATPLOTLIB METHOD (old version, youll have to import matplotlib)
while True:
    print("___Sharpening Values___(Expected type = float)")
    alpha = float(input("Enter Contrast: "))
    beta = float(input("Enter Brightness: "))
    print("___Blur Values___(Expected type = int and odd)")
    Dev = int(input("Enter Deviation: "))
    print("__Edge Detection__(Expected type = int)")
    lowThreshold = int(input("Lower Threshold: "))
    thresRatio = int(input("Threshold Ratio: "))

    #Display Stuff
    fig = plt.figure()

    a = fig.add_subplot(2,2,1)
    plt.imshow(img)
    a.set_title('Original Image')
    a.set_yticklabels([])
    a.set_xticklabels([])

    a = fig.add_subplot(2,2,2)
    plt.imshow(blur(img, Dev, Dev))
    a.set_title('Blurred Image')
    a.set_yticklabels([])
    a.set_xticklabels([])

    a = fig.add_subplot(2,2,3)
    plt.imshow(contraster(img, alpha, beta))
    a.set_title('Contrasted Image')
    a.set_yticklabels([])
    a.set_xticklabels([])
    
    a = fig.add_subplot(2,2,4)
    plt.imshow(edgeConverter(img,lowThreshold,thresRatio))
    a.set_title('edgeConvertered Image')
    a.set_yticklabels([])
    a.set_xticklabels([])

    plt.show()
    print("---------------------------------------------------------------------")
"""
