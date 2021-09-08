L = [1,1,2,3,4,5,4]
for i in range(len(L)):
    if L.count(L[i]) > 1:
        L.remove(L[i])
print(L)
