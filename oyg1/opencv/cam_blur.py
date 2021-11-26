import cv2
import numpy as np

cam = cv2.VideoCapture(-1)
while True:
    ret,im = cam.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(im,50,70) 
    # cv2.imshow("normal",im)
    # im_b=cv2.blur(im,(5,5))
    # cv2.imshow("blur",im_b)
    # im_g=cv2.GaussianBlur(im,(5,5),0)    
    # cv2.imshow("gausian_blur",im_g)
    # im_m=cv2.medianBlur(im,7)
    # cv2.imshow("median blur",im_m)

    cv2.imshow("normal",gray)
    cv2.imshow("canny",canny)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
