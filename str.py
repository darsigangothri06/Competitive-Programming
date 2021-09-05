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

'''














