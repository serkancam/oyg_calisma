dizi = [43,10,17,42,2,36,17,20,30,22,50,60]

for i in range(len(dizi)):  
    for j in range(i+1,len(dizi)):
        if dizi[i] % dizi[j] ==0 or dizi[j] % dizi[i]==0:
            print(dizi[i],"-",dizi[j])

