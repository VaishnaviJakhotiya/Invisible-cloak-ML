import cv2
import numpy as np
cap = cv2.VideoCapture(0) # 0 to capture from webcam
background_image = cv2.imread('image.jpg') # reading background image that was taken earlier

while True:
    ret, frame = cap.read()

    if ret:
        frametohsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # to convert frame from RGB to HSV
        
        lower_red = np.array([0,100,100])
        upper_red = np.array([10,255,255])
        # lower and upper threshold bound for red colour

        redmask = cv2.inRange(frametohsv,lower_red,upper_red) # mask for detecting red colour
        redmask = cv2.morphologyEx(redmask,cv2.MORPH_OPEN, np.ones((7,7),np.uint8)) # to remove noise from mask
        
        background_redmask = cv2.bitwise_and(background_image,background_image, mask=redmask) 
        # highlights red colour things in background (shows everything behind red mask in background)   

        not_redmask= cv2.bitwise_not(redmask) # not red
        
        frame_notredmask= cv2.bitwise_and(frame, frame, mask=not_redmask) 
        # hides red colour things in current frame (shows everything not red in frame)
        
        cv2.imshow("cloak",  background_redmask + frame_notredmask) # background image over red colour in current frame
        
        if cv2.waitKey(2) == ord('y'): # if y is pressed on keyboard
            break
cap.release()
cv2.destroyAllWindows()