import cv2
import numpy as np
import os
# Load the image
cd = os.getcwd()
image_path=os.path.join(cd,"opencv","images","chp2","nature.jpg")
image = cv2.imread(image_path)
cv2.imshow("Original  Image", image)

#Define the kernel
fileteredImag5 = cv2.bilateralFilter(image, 5, 150,50)
cv2.imshow("Blurred image 5", fileteredImag5)

fileteredImag7 = cv2.bilateralFilter(image, 7, 150,50)
cv2.imshow("Blurred image 7", fileteredImag7)


cv2.waitKey(0)
# Önceki üç bulanıklaştırma tekniği, görüntüdeki kenarları kaybettiğimiz yan etkiyle bulanık görüntüler verir. Kenarları korurken bir görüntüyü bulanıklaştırmak için, Gauss bulanıklığı üzerinde bir geliştirme olan iki taraflı bulanıklaştırma kullanıyoruz. İki taraflı bulanıklaştırma, hesaplamayı gerçekleştirmek için iki Gauss dağılımını gerektirir.
