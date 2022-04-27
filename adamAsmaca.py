# -*- coding: utf-8 -*-
import random
tahminler=[]
bilinenler=[]
dosya=open("sorular.txt","r")
sorular=dosya.readlines()
r=random.randint(1,len(sorular)-1)
cumle=sorular[r].lower()
print(cumle)

def yazdir():
    tahmin=""
    for h in cumle:
        if h==" ":
            tahmin=tahmin+"  "
        elif h in bilinenler:
            tahmin=tahmin+h
        elif h=="\n":
            continue
        else:
            tahmin=tahmin+"_ "
    print(tahmin)
    return tahmin
yazdir()

while True:
    harf=input("lütfen bir harf giriniz:").lower()
    if harf=="-1":
        break
    
    if(len(harf)!=1) or (harf in tahminler) or(harf==" "):
        print("daha önce söylenmeyen veya başka bir harf giriniz:")
        continue
    tahminler.append(harf)
    if harf in cumle:
        bilinenler.append(harf)
    kontrol=yazdir()
    if "_" not in kontrol:
        print("tebrikler")
        break
        
    
    
    
    
    
    
    
    
    
    
    
    

        
        
        
    