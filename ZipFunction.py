'''
L1 = [10,20,30]
L2 = list(map(lambda n:n+1, L1))
for i,j in zip(L1,L2):
    print(i,"----->", j)
print()

L1 = [10,20,30,50,70,100]
print(L1,L1[2:])
L2 = list(map(lambda n:n+1, L1[2:]))
for i,j in zip(L1,L2):
    print(i,"----->", j)
'''
a = 23
def inc():
    global a
    a = a + 2
    print(a)
inc()