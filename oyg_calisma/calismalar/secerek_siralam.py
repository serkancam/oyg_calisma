A = [43,1,17,42,2,36,17,20,30,22,50,60]

for i in range(len(A)):
    ek= i
    for j in range(i+1, len(A)):
        if A[ek] > A[j]:
            ek = j
    A[i], A[ek] = A[ek], A[i]
# main
for i in range(len(A)):
   print(A[i])