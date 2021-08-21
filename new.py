'''
num = input()
rev = num[::-1]
diff = abs(int(num) - int(rev))
cnt = 0
while diff % 2 == 0:
    cnt += 1
    diff = diff / 2
print(cnt)
'''
size = list(map(int,input().split()))
L = []
for i in range(size[0]):
    k = list(map(int,input().split()))
    L.append(k)
X = int(input())
cnt = 0
print(L)
if size[0] > size[1]:
    for i in range(len(L)):
        L[i].append(1)
else:
    k = [1 for i in range(size[1])]
    L.append(k)
print(L)
for i in range(len(L)):
    for j in range(len(L)):
        if i != j:
            m = L[i][j]
            print(m)
            if L.count(m) > X:
                print(L[i][j])
                cnt += L[i][j]
print(cnt)
