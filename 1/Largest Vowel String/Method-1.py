Str = input("Enter a string: ")
vowl = 'aeiou'
p = ''
for i in range(len(Str)):
    if Str[i] in vowl:
        for j in range(i+1,len(Str)):
            if Str[j] in vowl and len(set(Str[i:j])) <= len(set(vowl)) and len(p) < len(Str[i:j]):
                p = Str[i:j]
    else:
        continue
print(p)

# we have to use while loop