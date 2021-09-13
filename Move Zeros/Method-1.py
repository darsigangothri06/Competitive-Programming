L = list(map(int,input().split()))
p = len(L)
for i in range(len(L)):
    if L[i] == 0:
        for j in range(i+1,p):
            L[i],L[j] = L[j],L[i]
        p = p - 1
print(L)
