L = list(map(int,input("Enter comma-separated integers: ").split(',')))
cnt = 0 # to count even numbers
y = 0  # to break loop if swaps occur cnt times
for i in L:
    if i % 2 == 0:
        cnt += 1
for i in range(len(L)):
    if L[y] % 2 == 0:
        break
    # finding p index
    for k in range(len(L)-1,0,-1):
        if L[k] % 2 == 0:
            p = k
            break
    if L[i] % 2 != 0:
        L[i],L[p] = L[p],L[i]
        y += 1
    if y == cnt:
        break
print(L)
