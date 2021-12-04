'''
def Conv(s):
    return int(s)
Inp = input("Enter space separated digits: ").split()
L = []
for i in Inp:
    L.append(Conv(i))
print(L)

'''
num = int(input("Enter number of digits to enter: "))
L = []
for i in range(num):
    x = int(input("Enter: "))
    L.append(x)
print(L)