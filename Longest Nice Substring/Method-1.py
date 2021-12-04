s = "baBaacCb"
Nice = ''
curr = ''
for i in s:
    if curr == '':
        curr += i
    else:
        p = i.lower()
        if curr[-1] == p or curr[-1] == p.upper():
            curr += i
        else:
            if len(set(curr)) == 2 and len(curr) > len(Nice):
                Nice = curr
            curr = i
if len(set(curr)) == 2 and len(curr) > len(Nice):
    Nice = curr
print(Nice)
