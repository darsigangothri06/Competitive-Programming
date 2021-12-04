n = 4
L = [2,2,1,1]
Req = []
for i in range(n//2):
    Req.append(max(L))
    L.pop(L.index(max(L)))
print(sum(Req) - sum(L))
    