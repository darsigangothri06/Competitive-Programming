L1 = list(map(int,input("Enter space separated list1: ").split()))
L2 = list(map(int,input("Enter space separated list2: ").split()))
L3 = [i for i in L2 if i not in L1]
New = [i for i in L1 if i not in L2]
print(len(New)+len(L3))
