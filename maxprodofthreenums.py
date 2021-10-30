l = [-1,2,3,6,-2,-12,45]
l.sort()
print('l',l)
l1 = []
l2 = []
for i in range(len(l)):
    if l[i] < 0:
        l1.append(l[i])
    else:
        l2.append(l[i])
print('l1,l2',l1,l2)
if len(l) == len(l1):
    print(l[-1]*l[-2]*l[-3])
else:
    if len(l1) >= 2:
        print(l1[0]*l1[1]*l2[-1])
    else:
        print(l2[-1]*l2[-2]*l2[-3])        
