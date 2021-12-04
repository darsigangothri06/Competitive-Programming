Elements = list(map(int,input().split(',')))
Order = int(len(Elements)**0.5)
Matrix = []
Required = []

for i in range(0,len(Elements),Order):
    Matrix.append(Elements[i:i+Order])

Swap = True
while Matrix != []:
    if Swap:
        Required.extend(Matrix[0])
        Matrix.pop(0)
        for k in range(len(Matrix)):
            if Matrix[k] == []:
                break
            Required.append(Matrix[k][-1])
            Matrix[k] = Matrix[k][:-1]
        Swap = False
    else:
        Required.extend(Matrix[-1][::-1])
        Matrix.pop(-1)
        for k in range(len(Matrix)-1,-1,-1):
            if Matrix[k] == []:
                break
            Required.append(Matrix[k][0])
            Matrix[k] = Matrix[k][1:]
        Swap = True
print(','.join(map(str,Required)))
