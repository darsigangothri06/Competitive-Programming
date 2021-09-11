Str = list('zohomail')  # taking input as a list -- easy to swap two vowels
v = ['a','e','i','o','u']
i = 0
j = len(Str)-1
while i < len(Str):
    if Str[i] in v:
        if Str[j] in v:
            Str[i],Str[j] = Str[j], Str[i]
            j = j - 1
            i = i + 1
        else:
            j = j - 1
    else:
        i = i + 1
    if j < i:
        break
print(''.join(Str))
