def Validate(s):
    if '-' in s:
        if (s.count('-') == 1) and s[0] != '-' and s[-1] != '-':
            pass
        else:
            return 0
    for i in range(len(s)):
        if s[i] in ['!', '.',',']:
            if i != len(s)-1:
                return 0
        if s[i].isupper() or s[i].isdigit():
            return 0
    return 1
sentence = "Cat and. d-og"
count = 0
for i in sentence.split():
    count += Validate(i)
print(count)