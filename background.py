import cv2
cap = cv2.VideoCapture(0) # 0 to capture video from webcam

while cap.isOpened(): 
    ret, back = cap.read() # back is readings from camera
    if ret: #ret is true if camera is on / reading something
        cv2.imshow("image", back) # displaying image
        if cv2.waitKey(5) == ord('q'): # if q is pressed on keyboard
            cv2.imwrite('image.jpg', back) # save the image being captured as image.jpg
            break

cap.release()
cv2.destroyAllWindows()