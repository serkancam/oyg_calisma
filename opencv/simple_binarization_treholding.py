import cv2
import os
import numpy as np

image_path = os.path.join(os.getcwd(),"opencv","images","chp2","scanned_doc.png")
image = cv2.imread(image_path)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Grayscale Receipt", image)

(T, binarizedImage) = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)
cv2.imshow("Binarized Receipt", binarizedImage)


(Ti, inverseBinarizedImage) = cv2.threshold(image, 60, 255, cv2.
THRESH_BINARY_INV)
cv2.imshow("Inverse Binarized Receipt", inverseBinarizedImage)
cv2.waitKey(0)
