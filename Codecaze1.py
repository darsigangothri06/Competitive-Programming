# even odd
S = '47771217'
def F(s):
    for i in s:
        if i not in ['4','7']:
            return False
    return True
if '4' not in S and '7' not in S:
    print('-1')
else:
    L = []
    D = {}
    Q = []
    Req = '-1'
    for i in range(len(S)):
        for j in range(i+1,len(S)+1):
            if S[i:j] not in L and F(S[i:j]):
                L.append(S[i:j])
    for i in L:
        D.update({i:S.count(i)})
    Max = max(D.values())
    P = sorted(D.items(), key=lambda x: (x[1],x[0]), reverse=True)
    x = P[0][0]
    if int(x) > int(Req):
        print(str(x))
    else:
        print(Req)
