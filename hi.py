'''
Str = input()
L = list(input().split())
p = ''
for i in range(len(Str)):
    if Str[i] not in L:
        p = p + Str[i]
print(p)

Str = speech.split()
word = input()
D = {}
for i in Str:
    D[i] = D.get(i,0) + 1
print(D.get(word,0))

L1 = [1,2,3,4]
L2 = [4,3,5,6]
k = []
for i in L1:
    if i in L2:
        if i not in k:
            k.append(i)
print(k)
'''
Num  = int(input())
L = []
for i in range(Num):
    k = input()
    L.append(k)
D = {}
for i in L:
    D[i] = D.get(i,0) + 1
print('A=',D['A'])
print('B=',D['B'])
print('C=',D['C'])
cnt = 0
print(D)
for i in D.keys():
    if i not in ['A','B','C']:
        cnt += D[i]
print('invalid',cnt)

