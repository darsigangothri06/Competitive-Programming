L = [1,3,3,4,5,2,1,8,3,1,4,3,1]
k = 3
cnt = 0
a = 0
for i in L:
    if i == k:
        cnt += 1
for i in range(len(L)):
    if L[i] == k:
        for j in range(len(L)-1,-1,-1):
            if L[j] != k:
                p = j
                break
        L[i],L[p] = L[p],L[i]
        a += 1
        print(L)
    if a == cnt//2:
        break
print(L)
