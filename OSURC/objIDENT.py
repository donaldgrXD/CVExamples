import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img2 = frame
    img1 = cv2.imread('yeet.png')
    #img2 = cv2.imread('image.png') # trainImage

    # Initiate ORB detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    matchesMask = [[0,0] for i in range(len(matches))]

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    draw_params = dict(matchColor = (0,255,0),
                       singlePointColor = (255,0,0),
                       matchesMask = matchesMask,
                       flags = 0)

    for a in range(0,len(kp2)-1):
        #print(kp2[a].pt[0],kp2[a].pt[0])
        a,b = int(kp2[a].pt[0]),int(kp2[a].pt[1])
        cv2.circle(img2,(a,b),3,(0,0,255),-1)
    
    # Draw first 10 matches.
    #img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2)
    #img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    #img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,flags=2)
    cv2.imshow('seperate',img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
