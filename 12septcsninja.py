L = list(map(int,input().split()))
cnt = 1
for i in range(1,len(L)):
    flag = 0
    for j in range(0,i):
        if L[j] > L[i]:
            flag = 1
            break
    if flag == 0:
        cnt += 1
print(cnt)
