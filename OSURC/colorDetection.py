import numpy as np
import cv2

cap = cv2.VideoCapture(0)

red = np.uint8([[[0,0,255]]])
green = np.uint8([[[0,255,0]]])
blue = np.uint8([[[255,0,0]]])

hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)

boundaries = {
    'red':[[[0, 0, 0],[10,255,255]],[[170,0,0],[180,255,255]]],
    'green':[[50,0,0],[70,255,255]],
    'blue':[[110,0,0],[130,255,255]]
    }

print("red",hsv_red,"\ngreen",hsv_green,"\nblue",hsv_blue)


while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower = np.array([110,50,50])
    #upper = np.array([130,255,255])
    """
    # lower mask (0-10)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    mask = mask1 + mask0
    """
    color = 'blue'

    if color == 'red':
        mask1 = cv2.inRange(hsv,np.array(boundaries['red'][0][0]), np.array(boundaries['red'][0][1]))
        mask2 = cv2.inRange(hsv,np.array(boundaries['red'][1][0]), np.array(boundaries['red'][1][1]))
        mask = mask1 + mask2
    else:
        mask = cv2.inRange(hsv,np.array(boundaries[color][0]), np.array(boundaries[color][1]))

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

