import numpy as np
import cv2

cap = cv2.VideoCapture(0)

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

cv2.namedWindow('image')
cv2.createTrackbar('BLUR','image',0,100,nothing)
cv2.createTrackbar('CONTRAST','image',1,10,nothing)
cv2.createTrackbar('BRIGHTNESS','image',0,100,nothing)
cv2.createTrackbar('EDGE_Threshold','image',0,200,nothing)
cv2.createTrackbar('EDGE_Ratio','image',0,10,nothing)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    blurTrack = cv2.getTrackbarPos('BLUR','image')
    contrastTrack = cv2.getTrackbarPos('CONTRAST','image')
    brightnessTrack = cv2.getTrackbarPos('BRIGHTNESS', 'image')
    thresholdTrack = cv2.getTrackbarPos('EDGE_Threshold', 'image')
    ratioTrack = cv2.getTrackbarPos('EDGE_Ratio','image')

    if blurTrack %2 == 0:
        blurTrack += 1

    proccessedImage = edgeConverter(blur(contraster(frame, contrastTrack, brightnessTrack), blurTrack, blurTrack),thresholdTrack, ratioTrack) #apply all filters
    proccessedImage = cv2.cvtColor(proccessedImage, cv2.COLOR_GRAY2RGB)
    shownImage = cv2.resize(np.hstack((frame,proccessedImage)), (0,0), fx=0.8, fy=0.8)
    
    # Display the resulting frame
    cv2.imshow('seperate',shownImage)
    #cv2.imshow('gray', gray)
    #cv2.imshow('frame2', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
