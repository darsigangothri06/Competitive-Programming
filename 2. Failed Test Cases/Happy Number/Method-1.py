def happy(num):
    if len(num) == 1 and int(num) == 1:
        return True
    elif len(num) == 1 and int(num) != 1:
        return False
    else:
        Sum = 0
        for i in num:
            Sum = Sum + int(i) * int(i)
        return happy(str(Sum))
print(happy(input("Enter a number: ")))
