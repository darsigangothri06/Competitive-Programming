L = list(map(int,input("Enter comma-separated integers: ").split(',')))
Emp = []
for i in range(len(L)):
    for j in range(i+1,len(L)):
        Emp.append(L[i]^L[j])
print(max(Emp))
