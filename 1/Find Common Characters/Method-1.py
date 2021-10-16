words = ["bella","label","roller"]
p = set(words[0])
length = len(words)
for i in range(1,length):
    p = p & set(words[i])
print(p)
