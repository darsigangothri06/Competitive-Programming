# for two digit number
num = input("Enter two digit number: ")
D = {1:list('ABC'), 2:list('DEF'), 3: list('GHI'), 4: list('JKL'), 5: list('MNO'), 6: list('PQR'), 7: list('STU'), 8: list('VWX'), 9: list('YZ')}
L = [] # to append keys
cnt = 0 # to count combinations
Com = []
for i in num:
    L.append(D[int(i)])
for i in range(len(L[0])):
    for j in range(len(L[1])):
        Com.append(L[0][i]+L[1][j])
        cnt += 1
print(Com)
print(cnt)
