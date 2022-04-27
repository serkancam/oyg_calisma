import cv2
import numpy as np
import os

#projenin ana path kısmı bulnuyot
cd  = os.getcwd()
# zebra.png olu bulunuyor
image_path = os.path.join(cd,"opencv","images","chp2","zebra.png")
# resim image değişkeneşine aktarılıyo (x,y,3)
image_original = cv2.imread(image_path)

# resim boyur bilgileri alınıyor
h,w,c = image_original.shape

# resim en boy oranı bulunuyor. önemli>
aspect = w/h # bu değer ratio belirteceği için ondalıklı olabilir.
# yeni boyut(dimension) hesaplayalım örneğin yükseliği yarısına düşürelim
# yeni ordanların tam sayı olması gerkmektdir.
h_new = int(0.2*h)
w_new = int(h_new*aspect)
dimension = (h_new,w_new)

# şimdi resmi yeni boyutu ile elde edelim
resized_image = cv2.resize(image_original,dimension,interpolation=cv2.INTER_AREA)
cv2.imshow("Original_image",image_original)
cv2.imshow("Resized image",resized_image)

cv2.waitKey(0)


# INTER_LINEAR: Bu aslında en yakın dört komşunun (2 × 2 = 4) belirlendiği ve bir sonraki pikselin değerini belirlemek için ağırlıklı ortalamasının hesaplandığı bir çift doğrusal enterpolasyondur. 

# INTER_NEAREST: Bu, o noktanın etrafındaki noktalarda (komşu) noktalarda o fonksiyonun değeri verildiğinde, bir boşluktaki bir olmayan nokta için bir fonksiyonun değerini tahmin etmek için en yakın komşu enterpolasyon yöntemini kullanır. Başka bir deyişle, bir pikselin değerini hesaplamak için, en yakın komşusunun enterpolasyon fonksiyonuna yaklaştığı kabul edilir. 

# INTER_CUBIC: Bu, piksel değerini hesaplamak için bikübik enterpolasyon algoritması kullanır. Çift doğrusal enterpolasyona benzer şekilde, bir sonraki pikselin değerini belirlemek için 4 × 4 = 16 en yakın komşuyu kullanır. Hız bir sorun olmadığında, bikübik enterpolasyon, çift doğrusal ile karşılaştırıldığında daha iyi yeniden boyutlandırılmış bir görüntü sağlar. 

# INTER_LANCZOS4: Bu, 8 × 8 en yakın komşu enterpolasyonunu kullanır. 

# INTER_AREA: Piksel değerinin hesaplanması, piksel alanı ilişkisi kullanılarak gerçekleştirilir (OpenCV resmi belgelerinde açıklandığı gibi). Bu algoritmayı hareli olmayan yeniden boyutlandırılmış bir görüntü oluşturmak için kullanıyoruz. Görüntü boyutu büyütüldüğünde, INTER_AREA INTER_NEAREST yöntemine benzer.