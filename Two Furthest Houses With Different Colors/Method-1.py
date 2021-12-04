colors = [1,0]
x = colors[0]
for i in range(len(colors)-1,0,-1):
    if colors[i] != x:
        print(colors[i],x)
        break
