import cv2 
import os

cd = os.getcwd()
im_path = os.path.join(cd,"numpy","bo2.png")
image = cv2.imread(im_path) 
kesik = image[::,::4]

# h, w = image.shape[:2] 
# Displaying the height and width 
# print(f"Height = {h},  Width = {w}") 
# print(cv2.__version__)

cv2.imshow("test",image)
cv2.imshow("kesik",kesik)
cv2.imwrite(os.path.join(cd,"numpy","bo2_kucuk3.png"),kesik) 
cv2.waitKey(0)

cv2.destroyAllWindows()