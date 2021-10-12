name = input()
typed = input()
M = [name[0]]
p = 0
for i in range(1,len(name)):
    if M[p] != name[i]:
        M.append(name[i])
        p += 1
L = [typed[0]]
p = 0
for i in range(1,len(typed)):
    if L[p] != typed[i]:
        L.append(typed[i])
        p += 1
print(M,L)
print('true') if ''.join(L) == name else print('false')
#leelee    lleeelee