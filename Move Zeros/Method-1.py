L = list(map(int,input().split()))
i = 0
j = len(L) - 1
while i < len(L):
    if L[i] == 0:
        if L[j] != 0:
            L[i],L[j] = L[j],L[i]
            print('swap',L)
            j = j - 1
            i = i + 1
        else:
            j = j - 1
    else:
        i = i + 1
    if j < i:
        break
print(L)
