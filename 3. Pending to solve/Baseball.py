L = input("Enter score: ").split()
N = []
for i in L:
    if i == '+':
        N.append(N[-1] + N[-2])
    elif i == 'C':
        N.pop()
    elif i == 'D':
        N.append(2*N[-1])
    else:
        N.append(int(i))
print(sum(N))