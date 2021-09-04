L = list(map(int,input().split()))
k = int(input())
for i in range(len(L)//2):
    ind = i + k
    L[ind],L[i] = L[i],L[ind]
    print(L)
print(L)
