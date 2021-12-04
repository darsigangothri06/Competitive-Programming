import itertools
L = []
Q = []
n = 1222311
for i in str(n):
    L.append(int(i))
for p,q in itertools.groupby(L):
    Q.append(tuple([len(list(q)),p]))
print(Q)
