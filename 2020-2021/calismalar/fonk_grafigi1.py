import matplotlib.pyplot as plt
# üstteki satırda grafik çizdirme matplotlib modlünün pylot moddülü plt takma adı ile ekleniyo
import numpy as np
# numpy modülü np takma adı ile ekleniyor

x = []  # x değişkeni boş liste değeri ile başlatılıyor
y = list()  # y değişkeni boş liste değeri ile başatılıyor ikiside aynı

for i in range(-100, 101, 1):  # -100'den başlayarak 101'kadar(100 hariç) birer birer artan döngü
    x.append(i)  # her döngü adımında ki i değişkeni değeri x listesine eklenir

for t in x:  # döngü değişkeni t her adımında x listesinin bir elemanın değerini alır
    islem = 2*t**5-3*t-5
    y.append(islem)  # hesaplanan işlem sonucu y listesine eklenir.

#pyplot modülünün plot methodu çizgi grafiği çiziyor.
# bunun için bu methoda x,y listeleri parametre olarak veriliyor
plt.plot(x, y)
plt.savefig("grafik_ismi.png")
#çizilen grafik verilen karakter dizisi(string) adıyla kodun çalıştığı dizine saklanıyor.
plt.show()#grafik ekranda gösteriliyor


