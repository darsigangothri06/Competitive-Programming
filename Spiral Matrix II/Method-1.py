n = int(input())
E = list(range(1,n**2+1))
matrix = []
for i in range(0,len(E),n):
    matrix.append([E[i:i+n]])
Required = []
Swap = True
while matrix != []:
    print('hi')
    if Swap:
        Required.extend(matrix[0])
        matrix.pop(0)
        for k in range(len(matrix)):
            if matrix[k] == []:
                break
            Required.append(matrix[k][-1])
            matrix[k] = matrix[k][:-1]
        Swap = False
    else:
        Required.extend(matrix[-1][::-1])
        matrix.pop(-1)
        for k in range(len(matrix)-1,-1,-1):
            if matrix[k] == []:
                break
            Required.append(matrix[k][0])
            matrix[k] = matrix[k][1:]
        Swap = True
print(Required)
