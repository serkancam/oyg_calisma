import cv2
import numpy as np
import os
# Load the image
cd = os.getcwd()
image_path=os.path.join(cd,"opencv","images","chp2","nature.jpg")
park = cv2.imread(image_path)
cv2.imshow("Original Park Image", park)

#Define the kernel
kernel = (3,3)
blurred3x3 = cv2.blur(park,kernel)
cv2.imshow("3x3 Blurred Image", blurred3x3)

blurred5x5 = cv2.blur(park,(5,5))
cv2.imshow("5x5 Blurred Image", blurred5x5)

blurred7x7 = cv2.blur(park, (7,7))
cv2.imshow("7x7 Blurred Image", blurred7x7)
cv2.waitKey(0)

# Ortalama alma tekniğinde, görüntünün küçük bir bölümünü, örneğin k × k pikselleri alırız. Görüntünün bu küçük kısmına kayan pencere adı verilir. Bu kayan pencereyi görüntünün soldan sağa ve yukarıdan aşağıya hareket ettiriyoruz. Bu k × k matrisin merkezindeki piksel, onu çevreleyen tüm piksellerin ortalaması ile değiştirilir. Bu k × k matrisine evrişim çekirdeği veya basitçe çekirdek de denir. Tipik olarak, bu çekirdek tek sayı olarak alınır, böylece belirli bir merkez hesaplanabilir. Çekirdek boyutu ne kadar büyükse, görüntü o kadar bulanık hale gelir. Örneğin, bir 5 × 5 çekirdek, 3 × 3 çekirdeğe kıyasla daha bulanık bir görüntü üretecektir.