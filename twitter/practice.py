# A = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3] #[1,1,2,3,4,5,6,9,10]
A = [3, 3, 3, 3, 3, 4, 5, 5, 5, 5]
A.sort()
print(A)
L = []
i=0
j=len(A) - 1
k = 6
o = 0
while i < j:
    if (A[i] + A[j]) == k:
        L.append((A[i],A[j]))
        i += 1
        j -= 1
    else:
        if (A[i] < (k - A[j])):
            i += 1
        else:
            if (A[i] > k - A[j]):
                j -= 1
    o += 1            
print(L)
#print(set(L))
print(o)
print(len(A))