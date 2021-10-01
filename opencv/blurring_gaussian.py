import cv2
import numpy as np
import os
# Load the image
cd = os.getcwd()
image_path=os.path.join(cd,"opencv","images","chp2","park.jpg")
image = cv2.imread(image_path)
cv2.imshow("Original Park Image", image)

#Define the kernel
GaussianFiltered = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Gaussian Blurred Image", GaussianFiltered)
cv2.waitKey(0)

# Gauss filtreleme, görüntü işlemede en etkili bulanıklaştırma tekniklerinden biridir. Bu, Gauss gürültüsünü azaltmak için kullanılır. Bu bulanıklaştırma tekniği, ortalama alma tekniğine kıyasla daha doğal bir yumuşatma sonucu verir. Bu filtrelemede, kutulu sabit çekirdek yerine bir Gauss çekirdeği sağlıyoruz