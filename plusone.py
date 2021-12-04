l=[1,3,1]
l1=str(l[-1]+l[-2])
l2=[]
if (len(l1))!=2:
    l[-1]=l[-1]+l[-2]
    print(l)
else: 
    s=str(l1)
    print('s',s)
    l2.append(s[-1])
    print('l2',l2)
    a=int(s[0])+l[-2]
    print('a',a)
    b=str(a)
    if (len(b))!=0:
        l2.append(a)
        l2.append(l[-3])
    l2.reverse()
    print('l2',l2)
    print(l2)
