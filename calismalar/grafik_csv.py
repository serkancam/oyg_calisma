import matplotlib.pyplot as plt

f= open("sinav.csv")
for x in f:
    print(x.rstrip("\n"))

f.close()

a=["hasan","hüseyin","can"]
b=[1,2,3]
c=[2,4,3]

plt.scatter(a,b,color="red")
plt.scatter(a,c,color="green")
plt.show()