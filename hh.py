L = list(map(int,input().split()))
cnt = 1
j = len(L)
for i in range(j-1):
    if L[i] < L[i+1]:
        print('cnt',cnt,L[i+1])
        cnt += 1
print(cnt)
