A = input("Enter string A: ")
B = input("Enter string B: ")
k =[]
cnt = 0
'''
for i in range(len(A)):
    for j in range(i+1,len(A)+1):
        if A[i:j] in B:
            k.append([A[i:j],len(A[i:j])])
p = [k[i][1] for i in range(len(k))]
if len(p):
    for i in range(len(k)):
        if len(k[i][0]) == min(p):
            cnt += 1
    print(cnt)
else:
    print(0)
'''
for i in set(A):
    if i in B:
        cnt += 1
print(cnt)

