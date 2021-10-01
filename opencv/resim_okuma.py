import cv2
import os
import numpy as np

cd = os.getcwd()
# print(cd)
image_path = os.path.join(cd,"opencv","images","chp1","marsrover.png")
# print(image_path)
image = cv2.imread(image_path)
image2 =image.copy()
# image = image[::2,::2,:]
print(type(image),image.dtype)
#resmin dizi oalrak boyutunun bulunması
shape = image.shape
print(shape)
h = shape[0]
w = shape[1]
print(f"resmin boyutu: {w}*{h}")

# bir pikselin renk bilgisi
ilk_renk = image2[0,0]
print(ilk_renk)
# bir grup pikselin rengini değiştirelim
image2[0:100,0:200]=ilk_renk

#bir çizgi çizelim c2.line(resim,start,end,color,thikness)
baslangic = (100,70)#orta nokta
bitis =(350,380)
cizgi_rengi = (0,255,0)
kalinlik = 5
cv2.line(image2,baslangic,bitis,cizgi_rengi,kalinlik)
#aynı değerler il ebir dikdörtgen çizelim
cv2.rectangle(image2,baslangic,bitis,cizgi_rengi,kalinlik)

cv2.imshow("islenmis goruntu",image2)
cv2.imshow("orjinal gotuntu",image)
cv2.waitKey(0)
