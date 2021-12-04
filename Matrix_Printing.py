L = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(L)):
    print(L[i][i])

print()

for i in range(len(L)-1,-1,-1):
    print(L[i][i])

for i in range(len(L)-1):
    print(L[i][-1])
print(L[-1][::-1])
