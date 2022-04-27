#%%
def topla(liste):
    toplam=0
    if isinstance(liste,dict):
        liste=liste.values()
    for i in liste:
        if isinstance(i, list) or isinstance(i,tuple) or isinstance(i,set):
            toplam+=topla(i)
        if isinstance(i,dict):
            toplam+=topla(list(i.values()))
        if isinstance(i, int) or isinstance(i,float):
            toplam+=i
        
    return toplam



if __name__=="__main__":
    t1 = ["12","ali",1,2.0,10] 
    t2 = (1,2,(10,3,{3,6,3}))
    t3 = {"a":1,"b":[t1,t2]}
    t4 = (1,2,[3,(4,5,{7,8}),{"a":12,"b":[3,8,[12]]}])
    t5 = [[9,8],[10,21]]
    print(topla(t1))#13.0
    print(topla(t2))#25
    print(topla(t3))#39.0
    print(topla(t4))#65
    print(topla(t5))



# %%
