nums = [3,2,1,5,4]
k = 2
cnt = 0
for i in set(nums):
    cnt += nums.count(i+1) + nums.count(i-1)
print(cnt)
