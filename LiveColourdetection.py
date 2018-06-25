import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass


cv2.namedWindow('Image')
cv2.createTrackbar('H','Image',0,180,nothing)
cv2.createTrackbar('S','Image',0,255,nothing)
cv2.createTrackbar('V','Image',0,255,nothing)
cv2.createTrackbar('H2','Image',0,180,nothing)
cv2.createTrackbar('S2','Image',0,255,nothing)
cv2.createTrackbar('V2','Image',0,255,nothing)


while True:
    

    ret, img= cap.read()
    frame=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    r=cv2.getTrackbarPos('H','Image')
    g=cv2.getTrackbarPos('S','Image')
    b=cv2.getTrackbarPos('V','Image')
    r1=cv2.getTrackbarPos('H2','Image')
    g1=cv2.getTrackbarPos('S2','Image')
    b1=cv2.getTrackbarPos('V2','Image')

    maskb=cv2.inRange(frame,np.array([r,g,b]),np.array([r1,g1,b1]))


    final=cv2.bitwise_and(frame,frame,mask=maskb)
    cv2.imshow('Image',final)

    if cv2.waitKey(1)==13:
        break



cap.release()
cv2.destroyAllWindows()

