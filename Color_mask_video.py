##############################################################################Import Essential Libraries
import cv2                                                      #For Image Processing
import numpy as np                                              #For working with matrices
cap = cv2.VideoCapture(0)
ret,original=cap.read()
cv2.imshow("original bg",original)#Creates an object to work with webcam in laptop
while(1):                                                       #Infinite Loop
    _, frame = cap.read()                                       #Obtain Image from webcam
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                #Convert the image to HSV image
    lower_blue = np.array([0,0,0])                            #Set lower bound to detect red color in hsv image
    upper_blue = np.array([1,1,255])                         #Set upper bound for the same
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
                                                                #Get the binary mask using inRange
    color_mask = cv2.bitwise_and(original,original,mask=mask)
    
    mask_inv=cv2.bitwise_not(mask)
    
    color_mask_inv = cv2.bitwise_and(frame,frame,mask=mask_inv)
    
    changed=cv2.add(color_mask,color_mask_inv)
                                                                            #Colored mask
                                                                   #Display all the images
    cv2.imshow('Mask',mask)                                     #
    cv2.imshow('color mask having bg in space of me',color_mask)
    
    cv2.imshow(' current frame without my region ',color_mask_inv)
    cv2.imshow('Changed',changed)
    k = cv2.waitKey(5) & 0xFF
    
    #Keyboard interrupt
    if k == ord('p'):                                                 #
        break                                                   #
cv2.destroyAllWindows()                                         #
cap.release()                                                   #
#################################################################
#Note
#Either comment Line 11 or comment out lines 15,16 and 17 and uncomment line 11
