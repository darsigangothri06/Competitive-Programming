L = list(map(int,input("Enter comma-separated integers: ").split(',')))
req = []
p = 0
for i in range(len(L)-1):
    flag = 0
    for j in range(i,i+3): # taking each set
        if L[j] % 2 == 0:
            flag = 1
            break
    if flag == 0:
        p = 1
        print(L[i:i+3])
if p == 0:
    print('false')