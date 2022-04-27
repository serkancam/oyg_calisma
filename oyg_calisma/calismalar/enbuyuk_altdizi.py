# %%
dizi = [-13, -3, 10, 100, -3, -3, 23, -18, 20, -50, -12, -5, -22, -15, -4, -7]


def enbuyukaltdizi(l):
    eniyi = suanki = 0
    for i in l:
        suanki = max(suanki + i, 0)
        eniyi = max(eniyi, suanki)
    return eniyi


print(enbuyukaltdizi(dizi))
# %%
dizi = [-13, -3, 10, 100, -3, -3, 23, -18, 20, -50, -12, -5, -22, -15, -4, -7]
i = j = 0
ilk = son = 0
eniyi = -10000000  # eksi sonsuz
suanki = 0
while i < len(dizi):
    j = i
    while j < len(dizi):
        suanki += dizi[j]
        if suanki > eniyi:
            eniyi = suanki
            ilk=i
            son=j
        j += 1
    i+=1
    suanki=0
print(eniyi,ilk,son)

    
    

# %%

print(bin(37))

# %%
