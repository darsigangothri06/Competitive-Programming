L1 = [1,1,2,3,4,5,5,7,6,9,10]
L2 = [11,12,13,45,6,7,18,19,20]
Emp = L1 + L2
cnt = 0
for i in Emp:
    if i not in L1 or i not in L2:
        cnt += 1
        print(i)
print(cnt)
