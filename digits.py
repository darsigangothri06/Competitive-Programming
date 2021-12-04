s = 'deepcompute is 5 year old company which has more than 60 employees'
L = []
for i in s:
    if i.isdigit():
        L.append(int(i))
print(L)
