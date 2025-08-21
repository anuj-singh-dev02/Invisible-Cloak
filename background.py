import cv2
# THIS IS WEBCAM
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back= cap.read()     # READING FROM WEBCAM, BACK IS WHAT WEBCAM IS READING., RET CHECKS IF THE READING IS SUCCESFUL OR NOT.
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):        #PRESS 'Q' TO SAVE THE IMAGE
            cv2.imwrite('image.jpg', back) 
            break                            

cap.release()
cv2.destroyAllWindows()