Str = list('zohomail')  # taking input as a list -- easy to swap two vowels
v = ['a','e','i','o','u']
p = len(Str)-1
for i in range(len(Str)):
    if Str[i] in v:
        for j in range(p,-1,-1):
            if Str[j] in v:
                print(j,'swap',Str[i],Str[j],Str)
                Str[i],Str[j] = Str[j],Str[i]
                p = j
print(Str)
