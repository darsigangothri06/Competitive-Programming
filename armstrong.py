num = input("Enter a number: ")
Sum = 0
for i in num:
    Sum += int(i)**3
print('true') if int(num) == Sum else print('false')
