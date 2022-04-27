import cv2
import numpy as np
import os
# Load the image
cd = os.getcwd()
image_path=os.path.join(cd,"opencv","images","chp2","salt-pepper.jpg")
image = cv2.imread(image_path)
cv2.imshow("Original  Image", image)

#Define the kernel

blurredImage3 = cv2.medianBlur(image, 3)
cv2.imshow("blurredImage3", blurredImage3)

blurredImage5 = cv2.medianBlur(image, 5)
cv2.imshow("blurredImage5", blurredImage5)


cv2.waitKey(0)


# Ortanca bulanıklaştırma, tuz ve biber türü gürültüyü azaltmak için etkili bir tekniktir. Ortalama bulanıklaştırma, çekirdeğin merkezi değerinin, çevreleyen piksellerin medyanı ile değiştirilmesi dışında ortalama bulanıklaştırmaya benzer.