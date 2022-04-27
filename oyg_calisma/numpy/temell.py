# %%
import numpy as np

listem = [1, 2, 3, [3, 5]]

nd1 = np.array(listem)

print(nd1)
print(type(nd1))  # ndarray  n dim , n değişken dimension
print(nd1.size)
print(nd1.shape)
print(np.__version__)

# %% boyut arttırark gidelim 0-d

nd2 = np.array(2)
print(nd2.size)
print(nd2.shape)
print(nd2.dtype)


# %% 1-d
nd3 = np.array([2, 2])
print(nd3.size)
print(nd3.shape)
print(nd3.dtype)

# %% 2-d
l2 = [[32, 12, 3, 8], [1, 2, 3, 4]]
nd4 = np.array(l2)
print(nd4.size)
print(nd4.shape)
print(nd4.dtype)
print(nd4[0:, 0:2])


# %% 3-d

image = np.random.randint(0, 255, size=(300, 300, 3), dtype=np.uint8)
print(image.size)
print(image.shape)
print(image.dtype)

listem = [[[[1, 2]]]]
nd5 = np.array(listem)
print(nd5.shape)
print(nd5.ndim)

# %% deneme

# %%
nd0 = np.array(2)
nd1 = np.array([2, 2])
nd2 = np.array([[32, 12, 3, 8], [1, 2, 3, 4]])
nd3 = np.array([[[1, 2], [3, 4]], [[11, 32], [33, 44]],
                [[111, 222], [333, 4444]]])

print("nd0, shape:", nd0.shape, "ndim:", nd0.ndim)
print("nd1, shape:", nd1.shape, "ndim:", nd1.ndim)
print("nd2, shape:", nd2.shape, "ndim:", nd2.ndim)
print("nd3, shape:", nd3.shape, "ndim:", nd3.ndim)

# %% Daha fazla boyut(dimension)

nd6 = np.array([i for i in range(25)], ndmin=6)
print("nd6, shape:", nd6.shape, "ndim:", nd6.ndim)


# %% indexing elemanlara ulaşma

nd7 = np.array([1, 2, 3, 4])
nd8 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
nd9 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(nd7[1])
print(nd8[1, 2])
print(nd9[0, 1, 2])

# %% slicing

nd10 = np.array([1, 2, 3, 4, 5, 6, 7])
nd11 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(nd10[2:4])
print(nd11[1, 1:4])
print(nd11[:, 2:4])

# %% tipler

# strings - used to represent text data, the text is given under quote marks. eg. "ABCD"
# integer - used to represent integer numbers. eg. -1, -2, -3
# float - used to represent real numbers. eg. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent a number in complex plain. eg. 1.0 + 2.0j, 1.5 + 2.5j

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

nd12 = np.array([1, 2, 3, 4, 5, 6, 7], dtype=np.float16)
print(nd12.dtype)
nd13 = np.array([1, 2, 3, 4, 5, 6, 7], dtype=np.string_)  # burada dönüşüm olur
print(nd13.dtype)
# %%
nd14 = np.array([1.1, 2.1, 3.1])

yeni_dizi = nd14.astype(int)
print(yeni_dizi, yeni_dizi.dtype)
print(yeni_dizi.base)


# %% kopya ve görüntü (copy and view)
# Bir dizinin kopyası ile görünümü arasındaki temel fark, kopyanın yeni bir dizi olması ve görünümün yalnızca orijinal dizinin bir görünümü olmasıdır.

# Kopya verinin sahibidir ve kopyada yapılan herhangi bir değişiklik orijinal diziyi etkilemeyecektir ve orijinal dizide yapılan herhangi bir değişiklik kopyayı etkilemeyecektir.

# Kopya verinin sahibidir ve kopyada yapılan herhangi bir değişiklik orijinal diziyi etkilemeyecektir ve orijinal dizide yapılan herhangi bir değişiklik kopyayı etkilemeyecektir.
n15 = np.array([1, 2, 3, 4, 5])
x = n15.copy()
y = n15.view()
n15[0] = 42

print(n15)
print(x, "--", x.base)
print(y, "--", y.base)

x[4] = 55
y[3] = 44
print(20*"-")
print("n15:", n15)
print("x:", x, "--", x.base)
print("y:", y, "--", y.base)
# %%  reshaping
nd16 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

yeni1 = nd16.reshape(4, 3)
yeni2 = nd16.reshape(2, 3, 2)

print("yeni1:", yeni1, sep="\n")
print("yeni2:", yeni2, sep="\n")
print(nd16.flatten())
print(nd16.ravel())
print(nd16.rotate())

# %% iterasyon nditer

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

# %%
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
# %% ndenumerate iteration

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
    print(idx, x)
# %%

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)

# %% skalar işlemler
import numpy as np

a = np.array([[1, 2],[3, 4]])
b = np.array([[40, 30],[20, 10]])

print("skaler işlemler:")
print("a+1:",a+1,end="\n\n")
print("a*2:",a*2,end="\n\n")
print("b/3:",b/3,end="\n\n")
print("b-2:",b-2,end="\n\n")

# print("b.sum:",b.sqrt())

print("\ndiziler arası işlemler\n")

print("a+b:",a+b,sep="\n")
print("a/b:",a/b,sep="\n")



# %% 
print("a.T:",a.T,sep="\n")#dizinin devriği
print("np.sum(b):",np.sum(b),sep="\n")#tüm elemanların toplamı
print("np.sqrt(b):",np.sqrt(b),sep="\n")#dizi elemanlarının karekökü
print("np.add(a,b):",np.add(a,b),sep="\n")#iki dizinin bir biri ile toplamı


# %% yeni liste oluşturma

nd0 = np.zeros((3,3),dtype=np.uint8)
nd1 = np.ones((3,3),dtype=np.float32)
nd2 = np.full((3,3),6)
nd3 = np.arange(0,100,5)
nd32 = np.arange(12)
nd4 = np.linspace(0,100,num=30,endpoint=True)
print(nd0)
print(nd1)
print(nd2)
print(nd3)
print(nd32)
print(nd4)
# %%
ndt1=nd32.copy()
ndt2=nd32.copy()
print(nd32,ndt1,ndt2,sep="\n")
ndt1.shape=(3,4)
ndt2.shape=(4,3)
print(ndt1)
print(ndt2)
ndt1.shape=(4,3)
print("ndt1:\n",ndt1)

# %%
