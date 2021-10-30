nums1 = [1]
nums2 = []
if nums2:
    k = len(nums1)-len(nums1)
    for i in range(k):
        nums1.pop(-1)
    nums1.extend(nums2)
    nums1.sort()
print(nums1)
