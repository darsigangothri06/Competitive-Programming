N = int(input("Enter height: "))
g = 1
for i in range(N):
    L = []
    for j in range(1,2*(i+1)):
        if j % 2 != 0:
            L.append(g)
            g += 1
        else:
            L.append('*')
    print(*L)
# with spaces
