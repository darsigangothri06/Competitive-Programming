s= 'Andhra Pradesh'
for i in range(len(s)):
    if s[i] == 'A':
        s = s[:i] + 'B' + s[i+1:]
print(s)
