s = ["H","a","n","n","a","h"]
p = 0
for i in range(len(s)-1,len(s)//2,-1):
    s[i],s[p] = s[p],s[i]
    p += 1
print(s)
    
