def isprime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
          return False
    return True
    
def tree(num,cnt=0):
    if isprime(num):
        return cnt
    else:        
        for i in range(num//2,1,-1):
            if num % i == 0:
                cnt += 1
                return tree(i,cnt)
print(tree(12))
