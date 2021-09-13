L = list(map(int,input().split()))
i = 0
print('init',L)
while i < len(L):
    if L[i] == 0:
        print('in',i,L[i])
        L.remove(L[len(L)-1])
        print('rem',L)
        L = L[:i+1] + [0] + L[i+1:]
        print('cut',L)
        i += 2
    else:
        i += 1
print(L)
