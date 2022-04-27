import cv2
import os
import numpy as np
# create a new canvas
canvas_r = np.zeros((200, 200, 3), dtype = "uint8")
canvas_c = canvas_r.copy()
start = (10,10)
end = (100,100)
center = end
radius = 50
color = (0,0,255)
thickness = 5
cv2.rectangle(canvas_r, start, end, color, thickness)
cv2.circle(canvas_c, center,radius, color, thickness)
cv2.imshow("rectangel", canvas_r)
cv2.imshow("circle", canvas_c)

cd = os.getcwd()
r_path=os.path.join(cd,"opencv","images","chp1","rectangle.jpg")
c_path=os.path.join(cd,"opencv","images","chp1","circle.jpg")
cv2.imwrite(r_path, canvas_r)
cv2.imwrite(c_path, canvas_c)
cv2.waitKey(0)