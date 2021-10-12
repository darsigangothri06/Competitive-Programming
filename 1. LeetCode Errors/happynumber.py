def happy(num,flag = 0):
    if len(num) == 1 and int(num) == 1:
        return True
    elif len(num) == 1 and int(num) != 1 and flag > 0:
        return False
    else:
        flag = 1
        Sum = 0
        for i in num:
            Sum = Sum + int(i) * int(i)
        print(Sum)
        return happy(str(Sum),flag)
print(happy(input("Enter a number: ")))
# 1111111 expected true -- but my o/p is false