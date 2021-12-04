from functools import reduce
L = [12,23,45,1,2,5]
res = reduce(lambda a,b:a+b, L)
print(res)

res = reduce(lambda a,b:a if a>b else b, L)
print(res)

res = reduce(lambda a,b:a if a<b else b, L)
print(res)