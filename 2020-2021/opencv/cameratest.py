import cv2

cam = cv2.VideoCapture(-1)
while True:
    ret,im = cam.read()
    cv2.imshow("insan",im)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
