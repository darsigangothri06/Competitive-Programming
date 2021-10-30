arr = [2,2,2,3,3,4,4,5,5,8]
M = 2
X = len(arr)
D = []
for i in set(arr):
    D.append([arr.count(i),i])
K = sorted(D,reverse = True)
for i in range(M):
    count = K[i][0]
    X -= count
print(X)
