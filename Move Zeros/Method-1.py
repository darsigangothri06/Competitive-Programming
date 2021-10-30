L = [0,1,3,0,5,0,6,7]
print('re',[1,3,5,6,7,0,0,0])
c = 0
p = len(L)
for i in range(p):
    print('in',i,L)
    print('in',L[i])
    if L[i] == 0:
        print(i,L[i])
        L.pop(i)
        print(L)
        c += 1
for i in range(c):
    L.append(0)
print(L)
