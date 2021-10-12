L = list(map(int,input("Enter comma-separated integers: ").split(',')))
for i in L:
    if L.count(i) == 2:
        print(i)
        break