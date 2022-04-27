import cv2
import numpy as np
img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')
vis = np.concatenate((img1, img2), axis=1)
cv2.imwrite('out.png', vis)