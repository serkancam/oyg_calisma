
# -*- coding: utf-8
# %%

def karilastir(kelime, pivot):
    kelime = kelime.lower()
    pivot = pivot.lower()
    alfabe = " abcçdefgğhıijklmnoöprsştuüvyz"
    donus = True
    klen = len(kelime)
    plen = len(pivot)
    uzunluk = min(klen, plen)

    for i in range(uzunluk):
        # print(kelime,pivot)
        ki = alfabe.index(kelime[i])
        pi = alfabe.index(pivot[i])
        if ki == pi:
            continue
        elif ki > pi:
            donus = False
            break
        elif ki < pi:
            break

    if i == uzunluk-1 and klen > plen:
        donus = False
    return donus


def qsozcuk_sirala(sozluk: list):
    if len(sozluk) < 2:
        return sozluk
    else:
        pivot = sozluk[0]
        sol = [kelime for kelime in sozluk[1:]
               if karilastir(str(kelime), str(pivot))]
        sag = [kelime for kelime in sozluk[1:]
               if not karilastir(str(kelime), str(pivot))]

    return qsozcuk_sirala(sol) + [pivot] + qsozcuk_sirala(sag)


dosya = open(file="sozluk_sirasiz.txt", mode="r", encoding="utf-8")

s = dosya.readlines()
sozluk = []
dosya.close()
for i in range(len(s)):
    sozluk.append(s[i].strip().lower())

# sozluk=["ali","veli","aliye","deli"]
# # print(karilastir("ALİMe","aLi"))
# print(sozluk)
sirali = qsozcuk_sirala(sozluk)

print(*sirali, sep="\n")


# %%

ad = "ali".zfill(5)

print(len(ad), ad)

# %%
