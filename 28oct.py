'''
def triplets(t,d):
    Cnt = 0
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if d[i]+d[j]+d[k] <= t:
                    Cnt += 1
    return Cnt

s = 'AZGB'
total_seconds = 0
pointer = 'A'
for ch in s:
    if pointer == ch:
        total_seconds += 1
    else:
        diff = abs(ord(ch) - ord(pointer))
        total_seconds += min(diff, 26 - diff) + 1
        pointer = ch
print(total_seconds-len(s))

d = [1,2,3,4,5]
t = 8
d.sort()
Cnt = 0
n = len(d)
for i in range(0,n-2):
    j = i + 1
    k = n-1
    while(j < k):
        if (d[i]+d[j]+d[k] > t):
            k = k-1
        else:
            Cnt += (k - j)
            j = j+1
print(Cnt)
'''
