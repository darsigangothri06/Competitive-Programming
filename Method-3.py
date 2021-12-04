s = 'ssaeed'
s1 = 'ssaeed'
l = []
for i in range(len(s1)):
    if i < len(s1) - 1:
        if s1[i] == s1[i+1]:
            continue
        else:
            l.append(s1[i])
l.append(s1[-1])
s2 = ''.join(l)
print(l)
print(s2 == s)
