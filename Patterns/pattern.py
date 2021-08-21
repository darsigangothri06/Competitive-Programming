h = int(input())
for i in range(1,h+1):
    k = i
    L = [i,1]
    p = i
    for j in range(3,h+1):
        L.append(p)
        p *= k
    print(','.join(map(str,L)))
