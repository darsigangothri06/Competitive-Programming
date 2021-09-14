S = input()
for i in range(len(S)):
    if S[i] == '#':
        print(i)
        print('rep',S[i])
        S = S.replace((S[i-1]+S[i]),'')
        print('new',S)
print(S)
