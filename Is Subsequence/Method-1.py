s = "b"
t = "c"
Order = []
curr = 0
for i in range(len(s)):
    if s[i] not in t:
        print(False)
        break
    ind = t.find(s[i],curr)
    Order.append(ind)
    curr = ind
print(Order == sorted(Order))
