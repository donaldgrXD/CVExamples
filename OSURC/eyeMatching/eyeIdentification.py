import numpy as np
import pyautogui as pag
import cv2
import datetime
from time import sleep


def edgeConverter(img, lowThreshold = 120, thresRatio = 1):
    edges = cv2.Canny(img, lowThreshold, lowThreshold*thresRatio)
    return edges


template = cv2.imread("eyeTemplate.jpg")
#template = edgeConverter(template)

cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #frame = edgeConverter(frame)

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    w,h = template.shape[0:2]
    res = cv2.matchTemplate(frame, template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.75
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

"""
for a in images:
    print("___A___")
    image = cv2.imread("minesweeper1.PNG")
    
    boxTemplate = a

    w,h = boxTemplate.shape[0:2]
    res = cv2.matchTemplate(image, boxTemplate,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    cv2.imshow('boxes',image)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    
"""
"""
while(True):
    print(datetime.second)
    screen =  pag.screenshot()
    gray = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    cv2.imshow('window',gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
"""
