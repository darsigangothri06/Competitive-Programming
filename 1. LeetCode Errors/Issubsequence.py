ms = input("Enter a string: ")
ss = input("Enter subsequence: ")
flag = 0
ind = 0
for i in range(len(ss)):
    cnt = ind
    if ss[i] in ms:
        ind = ms.index(ss[i])
        if cnt > ind:
            flag = 1
            break
    else:
        flag = 1
        break
if flag == 0:
    print('true')
else:
    print('false')