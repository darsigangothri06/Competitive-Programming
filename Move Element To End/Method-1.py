# taking new list -- iterative method
L = [1,2,1,1,3,4,1]
S = L.copy()
tomove = 1
Emp = []
for i in range(len(L)):
    if L[i] != tomove:
        Emp.append(L[i])
        S.remove(L[i])
Emp.extend(S)
print(Emp)
