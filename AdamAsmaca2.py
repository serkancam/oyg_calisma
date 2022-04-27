tahminler=[]
bilinenler=[]
kontrol=""
dosya= open("cumle.txt", "r")
cumle=dosya.read()
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
    harf=input("bir harf tahmini giriniz:").lower()  
    if harf=="-1":
        break
    elif (len(harf)!=1) or (harf in tahminler) or (harf==" "):
        print("daha önce söylenmeyen tek bir harf giriniz:")
        continue
    tahminler.append(harf)
    if harf in cumle:
        bilinenler.append(harf)
    kontrol=yazdir()
    if "_" not in kontrol:
        print("Tebrikler kazandın")
        break
    
        
    


