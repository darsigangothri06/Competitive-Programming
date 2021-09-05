'''
Str = input()
K = ''
for i in Str:
    if i.isalpha():
        if ord(i) >= 65 and ord(i) <= 90:
            K += str(ord(i) - 64)
        else:
            K += str(ord(i) - 96)
    else:
        K += i
print(K)

L = input().split(',')
P = []
Q = []
for i in L:
    if i == 'E' and Q != []:   
            P.append(min(Q))
            Q.remove(min(Q))
    elif i != 'E':
        Q.append(int(i))
print(','.join(map(str,P)))

from itertools import permutations
Str = input()
Str2 = input()
L = [''.join(p) for p in permutations(Str)]
if Str2 in L:
    print('true')
else:
    print('false')
'''
from statistics import median
L = input().split(',')
L = list(map(int,L))
K = int(L[0])
L.remove(L[0])
print(L)
Q = []
for i in range(1,K):
    j = L[:i]
    Q.append(int(median(j)))
    '''
A = [L[0]]
B = [L[0],L[1]]
Q = []
Q.extend([int(median(A)),int(median(B))])

if len(L) % 2 != 0:
    print('od')
    '''
P = [int(median(L[i:i+K])) for i in range(len(L)-1)]
Q.extend(P)
print(Q)
'''
else:
    print('evee')
    P = [int(median(L[i:i+K])) for i in range(len(L))]
    Q.extend(P)
    print(Q)
    '''















